import numpy as np

def generate_prices(n_steps, initial_price=100, sigma=1.0, seed=None):
    if seed is not None:
        np.random.seed(seed)
    changes = np.random.normal(loc=0, scale=sigma, size=n_steps)
    prices = initial_price + np.cumsum(changes)
    return prices

def gaussian_walk(n, initial_price=100, sigma=1.0, seed=None):
    if seed is not None:
        np.random.seed(seed)
    changes = np.random.normal(loc=0, scale=sigma, size=n)
    return initial_price + np.cumsum(changes)

def gaussian_walk_with_trend(n, initial_price=100, sigma=1.0, mu=0.1, seed=None):
    if seed is not None:
        np.random.seed(seed)
    changes = np.random.normal(loc=mu, scale=sigma, size=n)
    return initial_price + np.cumsum(changes)

def geometric_brownian_motion(n, initial_price=100, sigma=0.02, mu=0.001, dt=1, seed=None):
    if seed is not None:
        np.random.seed(seed)
    Z = np.random.normal(size=n)
    prices = [initial_price]
    for i in range(1, n):
        change = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[i]
        prices.append(prices[-1] * np.exp(change))
    return np.array(prices)

def mean_reverting(n, initial_price=100, theta=100, phi=0.9, sigma=2.0, seed=None):
    if seed is not None:
        np.random.seed(seed)
    prices = [initial_price]
    for i in range(1, n):
        noise = np.random.normal(0, sigma)
        next_price = theta + phi * (prices[-1] - theta) + noise
        prices.append(next_price)
    return np.array(prices)