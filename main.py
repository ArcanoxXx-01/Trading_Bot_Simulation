from market import generate_prices
from bot import TradingBot
from simulator import run_simulation, plot_results
from utils import print_summaries

# Parámetros
N = 300
initial_price = 100
sigma = 1.0
seed = 4
fee = 0.005

# Crear precios
prices = generate_prices(N, initial_price, sigma, seed=seed)

# Crear bots
bots = [
    TradingBot("Bot Conservador", 1000, buy_thresh=0.97, sell_thresh=1.03, fee=fee),
    TradingBot("Bot Agresivo", 1000, buy_thresh=0.99, sell_thresh=1.01, fee=fee),
]

# Simular
run_simulation(prices, bots)
plot_results(prices, bots)
print_summaries(bots, prices[-1])
