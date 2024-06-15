
import backtrader as bt
class firstStrategy(bt.Strategy):
    def __init__(self):
        # initializing rsi, slow and fast sma
        self.rsi = bt.indicators.RSI(self.data.close, period=21)
        self.fast_sma = bt.indicators.SMA(self.data.close, period=50)
        self.slow_sma = bt.indicators.SMA(self.data.close, period=100)
        self.crossup = bt.ind.CrossUp(self.fast_sma, self.slow_sma)

    def next(self):
        if not self.position:
            # BUYING Condition
            if self.rsi > 30 and self.fast_sma > self.slow_sma:  # when rsi > 30 and fast_sma cuts slow_sma
                self.buy(size=100)  # buying 10 quantities of equity
        else:
            # SELLING Condition
            if self.rsi < 70:  # when rsi is below 70 line
                self.sell(size=100)  # selling 10 quantities of equity