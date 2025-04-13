import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os

def run_simulation(prices, bots):
    for t, price in enumerate(prices):
        for bot in bots:
            bot.act(price, t)

def plot_results(prices, bots, save_path="figures/simulacion_trading.png"):
    colors = ['blue', 'green', 'orange', 'purple', 'brown', 'red']
    bot_info = []

    # Crear carpeta si no existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Crear figura
    fig = plt.figure(figsize=(14, 8))
    gs = GridSpec(2, 1, height_ratios=[3, 1])
    ax = fig.add_subplot(gs[0])
    ax.plot(prices, label="Precio del activo", color="black", linewidth=2)

    for i, bot in enumerate(bots):
        color = colors[i % len(colors)]

        buy_times = [t for t, a, _, _ in bot.history if a == "BUY"]
        sell_times = [t for t, a, _, _ in bot.history if a == "SELL"]
        buy_prices = [p for t, a, p, _ in bot.history if a == "BUY"]
        sell_prices = [p for t, a, p, _ in bot.history if a == "SELL"]

        ax.scatter(buy_times, buy_prices, marker="^", color=color, label=f"{bot.name} BUY", zorder=3)
        ax.scatter(sell_times, sell_prices, marker="v", facecolors='none', edgecolors=color,
                   label=f"{bot.name} SELL", zorder=3)

        summary = bot.summary(prices[-1])
        bot_info.append([
            bot.name,
            f"{bot.buy_thresh:.2f}",
            f"{bot.sell_thresh:.2f}",
            f"{bot.fee*100:.2f}%",
            str(summary["total_trades"]),
            f"${summary['cash']:.2f}",
            f"${summary['net_worth']:.2f}"
        ])

    ax.set_title("Simulación de Bots de Trading")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Precio")
    ax.grid(True)
    ax.legend(loc="upper left")

    # Tabla
    table_ax = fig.add_subplot(gs[1])
    table_ax.axis("off")

    col_labels = ["Bot", "Buy Thresh", "Sell Thresh", "Fee", "Trades", "Cash", "Net Worth"]
    table = table_ax.table(cellText=bot_info, colLabels=col_labels, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.1, 1.5)

    # Guardar figura
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"[✔] Gráfica guardada como: {save_path}")

    plt.show()