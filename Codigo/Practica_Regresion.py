# =============================================================================
# Autor: Yahir Fernando Vargas Calderon
# Número de Control: 25041098
# Carrera: Ingeniería en Sistemas Computacionales (2do Semestre)
# Materia: Probabilidad y Estadística
# Práctica: Regresión Lineal y Correlación
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

archivos_csv = [
    'Datos/grupo1.csv',
    'Datos/grupo2.csv',
    'Datos/grupo3.csv'
]

for idx, archivo in enumerate(archivos_csv, start=1):

    print(f"\n{'='*40}")
    print(f"ANÁLISIS DEL GRUPO {idx} - Archivo: {archivo}")
    print(f"{'='*40}")

    df = pd.read_csv(archivo)

    col_x = df.columns[0]
    col_y = df.columns[1]

    print("\n--- Descripción Estadística Inicial ---")
    print(df.describe())

    plt.figure(figsize=(10, 4))

    
    plt.subplot(1, 2, 1)
    plt.hist(
        df[col_y],
        bins=10,
        color='skyblue',
        edgecolor='black'
    )

    plt.title(f'Histograma de Calificaciones - Grupo {idx}')
    plt.xlabel('Calificación Final')
    plt.ylabel('Frecuencia')

    
    X = df[[col_x]]
    y = df[col_y]

    modelo = LinearRegression()
    modelo.fit(X, y)

    pendiente = modelo.coef_[0]
    intercepto = modelo.intercept_
    r_cuadrado = modelo.score(X, y)

    print("\n--- Resultados del Modelo de Regresión ---")
    print(f"Ecuación: y = {intercepto:.4f} + {pendiente:.4f}x")
    print(f"Pendiente: {pendiente:.4f}")
    print(f"Intercepto: {intercepto:.4f}")
    print(f"R²: {r_cuadrado:.4f}")

    
    correlacion, p_valor = pearsonr(df[col_x], df[col_y])

    print("\n--- Correlación de Pearson ---")
    print(f"r = {correlacion:.4f}")
    print(f"Valor p = {p_valor:.4e}")

    
    plt.subplot(1, 2, 2)

    plt.scatter(
        df[col_x],
        df[col_y],
        color='blue',
        label='Datos reales'
    )

    plt.plot(
        df[col_x],
        modelo.predict(X),
        color='red',
        linewidth=2,
        label='Línea de regresión'
    )

    plt.title(f'Regresión: Estudio vs Calificación - Grupo {idx}')
    plt.xlabel('Horas de Estudio')
    plt.ylabel('Calificación')
    plt.legend()

    plt.tight_layout()

    
    plt.savefig(
        f'Graficas/graficas_grupo_{idx}.png',
        dpi=300,
        bbox_inches='tight'
    )

    
    plt.close()

print("\nProceso terminado correctamente desde GitHub Actions.")