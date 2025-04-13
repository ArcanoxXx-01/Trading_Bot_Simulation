
class TradingBot:
    def __init__(self, name, cash, buy_thresh=0.98, sell_thresh=1.02, fee=0.0):
        self.name = name
        self.cash = cash
        self.position = 0
        self.last_buy_price = None
        self.buy_thresh = buy_thresh
        self.sell_thresh = sell_thresh
        self.fee = fee
        self.history = []

    def act(self, price, t):
        action = None
        if self.position == 0:
            # Comprar?
            if self.last_buy_price is None or price < self.last_buy_price * self.buy_thresh:
                amount = self.cash // (price * (1 + self.fee))
                if amount > 0:
                    cost = amount * price * (1 + self.fee)
                    self.position = amount
                    self.cash -= cost
                    self.last_buy_price = price
                    self.history.append((t, "BUY", price, self.cash))
                    action = "BUY"
        else:
            # Vender?
            if price > self.last_buy_price * self.sell_thresh:
                revenue = self.position * price * (1 - self.fee)
                self.cash += revenue
                self.history.append((t, "SELL", price, self.cash))
                self.position = 0
                action = "SELL"
        return action

    def net_worth(self, current_price):
        return self.cash + self.position * current_price

    def summary(self, final_price):
        return {
            "bot": self.name,
            "net_worth": self.net_worth(final_price),
            "cash": self.cash,
            "position": self.position,
            "final_price": final_price,
            "total_trades": len(self.history)
        }
