def run_simulation(prices, bot):
    for t, price in enumerate(prices):
        bot.act(price, t)
