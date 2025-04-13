# 🤖 Simulación de un Bot de Trading con Eventos Discretos

Este proyecto implementa una simulación de eventos discretos para analizar el comportamiento de un bot de trading bajo distintos escenarios de mercado. La idea surge como proyecto del curso de Simulación, y busca aplicar herramientas estadísticas reales para evaluar estrategias de inversión simples pero controlables.

---

## 📌 Objetivos del Proyecto

- Implementar un modelo de simulación para bots de trading.
- Evaluar diferentes configuraciones de bots (estrategias).
- Comparar el desempeño bajo distintos modelos de precios.
- Analizar cómo afecta el horizonte temporal (semana, mes, año).
- Aplicar técnicas estadísticas: bootstrap, tests de hipótesis, intervalo de confianza, etc.

---

## 📊 Funcionalidades implementadas

✅ Simulación de bots con lógica de umbrales y comisiones.

✅ Generadores de precios:

* Ruido gaussiano simple
* Tendencia agregada
* Movimiento browniano geométrico
* Procesos mean-reverting

✅ Múltiples simulaciones con distintas semillas.

✅ Estimación de error y criterio de parada automática.

✅ Bootstrap para estimar media, mediana e IC.

✅ Pruebas estadísticas:
* Shapiro-Wilk
* D’Agostino
* Mann-Whitney U
* KS-test

✅ Comparación entre estrategias.

✅ Comparación entre modelos de precios.

✅ Comparación entre horizontes temporales.

✅ Gráficas de portafolio, decisiones, evolución de trades.


## 📁 Estructura del Proyecto

```bash
trading_bot_simulation/ 
├── data/               # Resultados en CSV 
│   └── ...
├── figures/            # Gráficas generadas automáticamente 
│   └── ...
├── report/             # Informe en LaTeX
│   ├── informe.pdf
│   └── informe.tex
├── analysis.py         # Lógica de simulaciones múltiples, tests, bootstrap, paradas y más
├── bot.py              # Lógica del bot y sus decisiones 
├── experiments.py      # Scripts de prueba para análisis 
├── main.py             # Ejemplo de simulación básica 
├── market.py           # Generadores de precios (diferentes modelos) 
├── plotter.py          # Gráficas de desempeño, evolución, comparaciones 
├── requirements.txt    # Almecena las dependencias del proyecto
└── simulator.py        # Corre la simulación paso a paso 
```

---

## ⚙️ Cómo usar el proyecto

### 1. Clona el repositorio:

```bash
git clone https://github.com/ArcanoxXx-01/Trading_Bot_Simulation.git
cd Trading_Bot_Simulation
```
### 2. Instalar dependencias

2.1 Crear un entorno virtual de pytho (opcional)
```bash
python3 -m venv env
```
Activar el entorno virtual
``` bash
source env/bin/activate
```
2.2 Utilizar el siguiente comando para instalar todas las dependencias de manera automatica
```bash
pip install -r requirements.txt
```

## 👨‍💻 Autor

### Darío López Falcón 

Estudiante de Ciencias de la Computación de la Universidad de La Habana

1er Proyecto del curso de Simulación 2024–2025

## 📎 Licencia

MIT License