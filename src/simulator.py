def run_simulation(prices, bot):
    """recorre precios y llama a bot.act()"""
    for t, price in enumerate(prices):
        bot.act(price, t)
