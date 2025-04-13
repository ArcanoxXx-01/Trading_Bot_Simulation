import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def plot_bot_trades(prices, bots):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(prices, label="Precio", color="black")

    for bot in bots:
        buy_times = [t for t, a, _ in bot.history if a == "BUY"]
        sell_times = [t for t, a, _ in bot.history if a == "SELL"]
        buy_prices = [p for _, a, p in bot.history if a == "BUY"]
        sell_prices = [p for _, a, p in bot.history if a == "SELL"]

        ax.scatter(buy_times, buy_prices, marker="^", color="green", label=f"{bot.name} BUY", zorder=5)
        ax.scatter(sell_times, sell_prices, marker="v", color="red", label=f"{bot.name} SELL", zorder=5)

    ax.set_title("Simulación del Bot de Trading")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Precio")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


def plot_distribution(df, column="net_worth", save_path=None, title="Distribución de Ganancias"):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df[column], bins=20, color="skyblue", edgecolor="black", alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("Ganancia Final ($)")
    ax.set_ylabel("Frecuencia")
    ax.grid(True)
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"[✔] Gráfico guardado en: {save_path}")
    else:
        plt.show()


def trace_error_plot(error_trace):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(error_trace, label="Error estimado", color="orange")
    ax.axhline(y=100, color="red", linestyle="--", label="Margen tolerable d=100")
    ax.set_title("Convergencia del Error en la Estimación de Ganancia Promedio")
    ax.set_xlabel("Número de simulaciones")
    ax.set_ylabel("Error estimado ($)")
    ax.legend()
    ax.grid(True)

    # Guardar la imagen
    os.makedirs("/mnt/data/figures", exist_ok=True)
    plot_path = "/mnt/data/figures/convergencia_error_bot.png"
    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    plot_path

def plot_bootstrap_distribution(samples, real_value=None, ci=None, save_path=None, title="Distribución Bootstrap"):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(samples, bins=30, color="skyblue", edgecolor="black", alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("Media de Ganancia")
    ax.set_ylabel("Frecuencia")
    if real_value:
        ax.axvline(real_value, color="green", linestyle="--", label="Valor observado")
    if ci:
        ax.axvline(ci[0], color="red", linestyle="--", label="IC 95%")
        ax.axvline(ci[1], color="red", linestyle="--")
    ax.legend()
    ax.grid(True)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"[✔] Gráfico guardado: {save_path}")
    else:
        plt.show()


def plot_portfolio_value(prices, bot, save_path=None):
    values = []
    for t, price in enumerate(prices):
        value = bot.cash + bot.position * price
        values.append(value)

    plt.figure(figsize=(10, 5))
    plt.plot(values, label="Valor del Portafolio", color="purple")
    plt.title(f"Valor del Portafolio - {bot.name}")
    plt.xlabel("Tiempo")
    plt.ylabel("Valor ($)")
    plt.grid(True)
    plt.legend()
    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


def plot_open_positions(prices, bot, save_path=None):
    positions = []
    for t, price in enumerate(prices):
        positions.append(bot.position)

    plt.figure(figsize=(10, 4))
    plt.plot(positions, label="Posiciones Abiertas", color="darkblue")
    plt.title(f"Posiciones Abiertas en el Tiempo - {bot.name}")
    plt.xlabel("Tiempo")
    plt.ylabel("Cantidad")
    plt.grid(True)
    plt.legend()
    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


def plot_investment_ratio(prices, bot, save_path=None):
    ratios = []
    for t, price in enumerate(prices):
        capital_total = bot.cash + bot.position * price
        invertido = bot.position * price
        ratio = invertido / capital_total if capital_total > 0 else 0
        ratios.append(ratio * 100)

    plt.figure(figsize=(10, 4))
    plt.plot(ratios, label="Capital Invertido (%)", color="green")
    plt.title(f"Porcentaje del Capital Invertido - {bot.name}")
    plt.xlabel("Tiempo")
    plt.ylabel("Porcentaje (%)")
    plt.grid(True)
    plt.legend()
    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


def plot_price_model_comparison(resultados_dict, metric="net_worth", save_path=None, title=None):
    """
    resultados_dict: dict con nombre del modelo como clave y DataFrame como valor
    metric: columna del DataFrame que se quiere graficar ("net_worth", "trades", etc.)
    """
    df_all = []
    for modelo, df in resultados_dict.items():
        temp = df[[metric]].copy()
        temp["Modelo"] = modelo
        df_all.append(temp)

    df_plot = pd.concat(df_all, ignore_index=True)

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df_plot, x="Modelo", y=metric, palette="Set2")
    plt.title(title or f"Comparación del Bot según el Modelo de Precios ({metric})")
    plt.ylabel(metric.replace("_", " ").capitalize())
    plt.grid(True)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        print(f"[✔] Guardado en {save_path}")
    else:
        plt.show()