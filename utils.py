
def print_summaries(bots, final_price):
    print("Resumen de Resultados:\n")
    for bot in bots:
        summary = bot.summary(final_price)
        print(f"- {summary['bot']}:")
        print(f"    Valor final: {summary['net_worth']:.2f}")
        print(f"    Efectivo: {summary['cash']:.2f}")
        print(f"    Posición: {summary['position']} acciones")
        print(f"    Trades realizados: {summary['total_trades']}\n")
