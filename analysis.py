import numpy as np
import pandas as pd
from scipy.stats import shapiro, normaltest, ttest_ind, mannwhitneyu, ks_2samp
from bot import TradingBot
from market import generate_prices
import os

def simulate_multiple_runs(bot_config, n_runs=100, n_steps=300, sigma=1.0):
    """Ejecutar el bot muchas veces con distintas semillas."""
    results = []
    for seed in range(n_runs):
        bot = TradingBot(**bot_config)
        prices = generate_prices(n_steps, sigma=sigma, seed=seed)
        for t, price in enumerate(prices):
            bot.act(price, t)
        results.append({
            "seed": seed,
            "net_worth": bot.net_worth(prices[-1]),
            "trades": len(bot.history),
            "final_cash": bot.cash,
            "final_position": bot.position
        })
    return pd.DataFrame(results)

def test_normality(df, column="net_worth"):
    shapiro_stat, shapiro_p = shapiro(df[column])
    normaltest_stat, normaltest_p = normaltest(df[column])
    return {
        "shapiro": (shapiro_stat, shapiro_p),
        "normaltest": (normaltest_stat, normaltest_p)
    }

def simulate_until_confidence(bot_config, d=100, confidence=0.95, max_runs=1000, n_steps=300, sigma=1.0):
    """Simular al bot repetidas veces y detenerse automáticamente cuando el intervalo de confianza 
    para la ganancia promedio sea suficientemente pequeño:

        z⋅σ/sqrt(n)<d

    Args:
        d: el margen de error tolerable (ej. $100).

        z: valor crítico para tu nivel de confianza (1.96 para 95%).

        max_runs: número máximo de simulaciones antes de rendirse.  
    """
    from scipy.stats import norm
    z = norm.ppf(0.5 + confidence / 2)

    results = []
    net_values = []
    error_trace = []
    seed = np.random.randint(0, 100000)

    while True:
        bot = TradingBot(**bot_config)
        prices = generate_prices(n_steps, sigma=sigma, seed=seed)
        for t, price in enumerate(prices):
            bot.act(price, t)
        net = bot.net_worth(prices[-1])
        net_values.append(net)
        results.append({
            "seed": seed,
            "net_worth": net,
            "trades": len(bot.history),
            "final_cash": bot.cash,
            "final_position": bot.position
        })

        seed += 1
        n = len(net_values)
        std = np.std(net_values, ddof=1)
        error = z * std / np.sqrt(n)
        error_trace.append(error) # para poder crear la tabla de convergencia del errror

        if error < d or n >= max_runs:
            break        

    df = pd.DataFrame(results)
    return df, error, error_trace

def bootstrap_confidence_interval(data, n_bootstrap=1000, ci=0.95):
    samples = []
    n = len(data)
    for _ in range(n_bootstrap):
        resample = np.random.choice(data, size=n, replace=True)
        samples.append(np.mean(resample))
    lower = np.percentile(samples, (1 - ci) / 2 * 100)
    upper = np.percentile(samples, (1 + ci) / 2 * 100)
    return np.mean(samples), (lower, upper), samples

def compare_bots(df1, df2, metric="net_worth"):
    x = df1[metric].values
    y = df2[metric].values

    # Pruebas
    t_stat, t_p = ttest_ind(x, y, equal_var=False)
    u_stat, u_p = mannwhitneyu(x, y, alternative='two-sided')
    ks_stat, ks_p = ks_2samp(x, y)

    return {
        "t_test": (t_stat, t_p),
        "mann_whitney": (u_stat, u_p),
        "ks_test": (ks_stat, ks_p)
    }

