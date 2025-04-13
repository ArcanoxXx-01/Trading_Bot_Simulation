import numpy as np

def generate_prices(n_steps, initial_price=100, sigma=1.0, seed=None):
    if seed is not None:
        np.random.seed(seed)
    changes = np.random.normal(loc=0, scale=sigma, size=n_steps)
    prices = initial_price + np.cumsum(changes)
    return prices
