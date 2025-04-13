from analysis import *
from plotter import *
from analysis import *
from market import *
import pandas as pd


bot_config = {
    "name": "BotEstadistico",
    "initial_cash": 10000,
    "buy_thresh": 0.97,
    "sell_thresh": 1.03,
    "fee": 0.005
}

df = simulate_multiple_runs(bot_config, n_runs=100)

# plot_distribution(df, save_path="figures/distribucion_bot.png")

# # Guardar resultados
# df.to_csv("data/resultados_bot_estadistico.csv", index=False)

# # Test de normalidad
# stats = test_normality(df)
# print("Shapiro:", stats["shapiro"])
# print("D’Agostino:", stats["normaltest"])

# ======================================================================


# df, final_error, error_trace = simulate_until_confidence(bot_config, d=100, confidence=0.95)

# print(f"[✔] Simulaciones necesarias: {len(df)}")
# print(f"[±] Error final estimado: ${final_error:.2f}")

# df.to_csv("data/resultados_bot_parada.csv", index=False)
# plot_distribution(df, save_path="figures/distribucion_bot_parada.png")

# # trace_error_plot(error_trace)

# ===========================================================================

# # Métricas a analizar con bootstrap
# metrics = ["net_worth", "trades", "final_cash", "final_position"]

# for metric in metrics:
#     media, (low, high), samples = bootstrap_confidence_interval(df[metric].values)
    
#     print(f"\n📈 Métrica: {metric}")
#     print(f"    Media bootstrap: {media:.2f}")
#     print(f"    IC 95%: ({low:.2f}, {high:.2f})")

#     plot_bootstrap_distribution(
#         samples,
#         real_value=df[metric].mean(),
#         ci=(low, high),
#         save_path=f"figures/bootstrap_{metric}.png",
#         title=f"Distribución Bootstrap - {metric}"
#     )

# =============================================================================

# Configuraciones de bots distintos
# bot1 = {
#     "name": "BotConservador",
#     "initial_cash": 10000,
#     "buy_thresh": 0.98,
#     "sell_thresh": 1.02,
#     "fee": 0.005
# }

# bot2 = {
#     "name": "BotAgresivo",
#     "initial_cash": 10000,
#     "buy_thresh": 0.95,
#     "sell_thresh": 1.05,
#     "fee": 0.005
# }

# # Simular ambos
# df1 = simulate_multiple_runs(bot1, n_runs=100)
# df2 = simulate_multiple_runs(bot2, n_runs=100)

# # Comparar ganancias
# print("🔍 Comparación de ganancias (net_worth):")
# result = compare_bots(df1, df2, metric="net_worth")
# for name, (stat, p) in result.items():
#     print(f"{name:>15}: stat={stat:.4f}, p-value={p:.4e}")

# # Puedes guardar o graficar también
# df1.to_csv("data/bot_conservador.csv", index=False)
# df2.to_csv("data/bot_agresivo.csv", index=False)

# =====================================================================================

# generators = {
#     "Gaussiano": gaussian_walk,
#     "Con Tendencia": gaussian_walk_with_trend,
#     "Geom Brown": geometric_brownian_motion,
#     "Mean Revert": mean_reverting
# }


# resultados = {}

# for nombre, gen_func in generators.items():
#     df = simulate_multiple_runs(bot_config, n_runs=100, n_steps=300,
#                                 sigma=1.0 if nombre != "Geom Brown" else 0.02)
#     resultados[nombre] = df
#     print(f"🧪 {nombre}: media net worth = ${df['net_worth'].mean():.2f}")


# print("Comparación entre Gaussiano y Mean-Reverting:")
# result = compare_bots(resultados["Gaussiano"], resultados["Mean Revert"])
# for name, (stat, p) in result.items():
#     print(f"{name:>15}: stat={stat:.4f}, p-value={p:.4e}")

# plot_price_model_comparison(
#     resultados_dict=resultados,  # Este diccionario contiene los DataFrames por modelo
#     metric="net_worth",
#     save_path="figures/comparacion_modelos_networth.png",
#     title="Ganancia Final según el Modelo de Precios"
# )

# plot_price_model_comparison(
#     resultados_dict=resultados,
#     metric="trades",
#     save_path="figures/comparacion_modelos_trades.png",
#     title="Cantidad de Operaciones según el Modelo de Precios"
# )


# ===========================================================================================

horizontes = {
    "Semana": 50,
    "Mes": 200,
    "Año": 1000
}

resultados_horizonte = {}

for nombre, pasos in horizontes.items():
    df = simulate_multiple_runs(
        bot_config, n_runs=100, n_steps=pasos, sigma=1.0
    )
    resultados_horizonte[nombre] = df
    print(f"[📈] {nombre}: media = ${df['net_worth'].mean():.2f}, trades promedio = {df['trades'].mean():.2f}")

plot_price_model_comparison(
    resultados_dict=resultados_horizonte,
    metric="net_worth",
    save_path="figures/comparacion_horizontes_networth.png",
    title="Ganancia Final según el Horizonte de Simulación"
)

plot_price_model_comparison(
    resultados_dict=resultados_horizonte,
    metric="trades",
    save_path="figures/comparacion_horizontes_trades.png",
    title="Cantidad de Operaciones según el Horizonte"
)










