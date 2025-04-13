from market import generate_prices
from bot import TradingBot
from simulator import run_simulation
from plotter import plot_bot_trades

# Configuración de simulación
steps = 300
initial_price = 100
sigma = 1.0

# Crear serie de precios
prices = generate_prices(steps, initial_price=initial_price, sigma=sigma, seed=42)

# Configurar bot
bot = TradingBot(name="BotSimple", initial_cash=10000, buy_thresh=0.97, sell_thresh=1.03, fee=0.005)

# Ejecutar simulación
run_simulation(prices, bot)

# Graficar resultados
plot_bot_trades(prices, [bot])
