import alpaca_trade_api as tradeapi
class Martingale(object):
    def __init__(self):
        self.KEY='your api key'
        self.SECRET='your secret key'
        self.URL='https://paper-api.alpaca.markets'
        self.api=tradeapi.REST(self.KEY,self.SECRET,self.URL)
        self.symbol='IVV'
        self.current_order=None
        self.last_price=1

        try:
            self.position=int(self.api.get_position(self.symbol).qty)
        except:
            self.position=0
    def submit(self,target):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)
        delta=target-self.position
        if delta==0:
            return
            print("Proccessing the order for {}".format(target))
        if delta>0:
            buy_quant=delta
            if self.position<0:
                buy=min(abs(self.position),buy_quant)
            print("Buying {} shares".format(buy_quant))
            self.current_order=self.api.submit_order(self.symbol,buy_quant,'buy','limit','day',self.last_price)
        elif delta<0:
            sell_quant=abs(delta)
            if self.position>0:
                sell_quant=min(abs(self.position),sell_quant)
            print("Selling {} shares ".format(sell_quant))
            self.current_order=self.api.submit_order(self.symbol,sell_quant,'sell','limit','day',self.last_price)

if __name__=="__main__":
    t=Martingale()
    t.submit(5)
