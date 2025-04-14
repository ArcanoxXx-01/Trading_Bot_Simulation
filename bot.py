class TradingBot:
    """Bot con lógica de umbrales, comisión y registro de decisiones"""
    def __init__(self, name, initial_cash, buy_thresh, sell_thresh, fee=0.0):
        self.name = name
        self.cash = initial_cash
        self.position = 0
        self.last_buy_price = None
        self.buy_thresh = buy_thresh
        self.sell_thresh = sell_thresh
        self.fee = fee
        self.history = []

    def act(self, price, t):
        if self.position == 0:
            if self.last_buy_price is None or price < self.last_buy_price * self.buy_thresh:
                qty = self.cash // (price * (1 + self.fee))
                if qty > 0:
                    self.cash -= qty * price * (1 + self.fee)
                    self.position = qty
                    self.last_buy_price = price
                    self.history.append((t, "BUY", price))
        else:
            if price > self.last_buy_price * self.sell_thresh:
                self.cash += self.position * price * (1 - self.fee)
                self.history.append((t, "SELL", price))
                self.position = 0

    def net_worth(self, current_price):
        return self.cash + self.position * current_price
