#  Práctica Final: Regresión Lineal y Correlación

<div align="center">

| **Información Académica** | **Detalles del Estudiante** |
|:---|:---|
| **Institución:** | Instituto Tecnológico de Durango (ITD) |
| **Carrera:** | Ingeniería en Sistemas Computacionales (3er Semestre) |
| **Materia:** | Probabilidad y Estadística |
| **Docente:** | Dr. José Gabriel Rodríguez Rivas |
| **Alumno:** | Vargas Calderón Yahir Fernando |
| **No. de Control:** | `25041098` |

</div>

---

##  Tabla de Contenidos

1. [Introducción y Objetivo](#introduccion)
2. [Metodología y Herramientas](#metodologia)
3. [Diagrama Conceptual del Flujo de Trabajo](#diagrama)
4. [Visualización Gráfica de los Modelos](#graficas)
5. [Conclusión General](#conclusion)
6. [Estructura del Repositorio y Accesos Directos](#repositorio)

---

<a id="introduccion"></a>

##  1. Introducción y Objetivo

El presente proyecto tiene como propósito fundamental aplicar los conceptos de **Regresión Lineal Simple** y **Correlación de Pearson** para modelar y analizar el comportamiento entre dos variables cuantitativas continuas: las **horas de estudio** (variable independiente $x$) y la **calificación final obtenida** (variable dependiente $y$) en tres grupos de estudio experimentales. El proceso ha sido completamente automatizado mediante un script desarrollado en Python, asegurando la reproducibilidad y validación de los modelos.

---

<a id="metodologia"></a>

##  2. Metodología y Herramientas

Para llevar a cabo el análisis estadístico y la generación de modelos predictivos, se utilizaron las siguientes librerías especializadas del ecosistema de Python:

- **Pandas:** Carga, estructuración y manipulación de los datasets en formato CSV.
- **Scikit-Learn:** Ajuste y cálculo del modelo de regresión lineal simple, obteniendo la ecuación de la recta ($y = b_0 + b_1x$) y el coeficiente de determinación ($R^2$).
- **SciPy (stats):** Cálculo del coeficiente de correlación de Pearson ($r$) para medir la fuerza de la relación lineal y su respectivo valor de significancia ($p$-value).
- **Matplotlib:** Generación de histogramas de distribución y diagramas de dispersión con líneas de tendencia.

---

<a id="diagrama"></a>

##  3. Diagrama Conceptual del Flujo de Trabajo

Este diagrama ilustra el proceso completo de la práctica, desde la carga de datos hasta la obtención de los modelos estadísticos y la conclusión para cada grupo de estudio.

```mermaid
graph TD

    classDef mainStyle fill:#d4e157,stroke:#33691e,stroke-width:2px,color:#000000;
    classDef rootStyle fill:#eceff1,stroke:#455a64,stroke-width:2px,color:#000000;
    classDef g1Style fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#000000;
    classDef g2Style fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000000;
    classDef g3Style fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px,color:#000000;
    classDef concStyle fill:#ffcc80,stroke:#e65100,stroke-width:2px,color:#000000;
    classDef detailStyle fill:#ffffff,stroke:#333333,stroke-width:1px,color:#000000;

    A["Practica FINAL: Regresion Lineal y Correlacion<br/>Autor: Yahir Fernando Vargas Calderon<br/>No. Control: 25041098"]:::mainStyle --> B["Analisis de Resultados"]:::rootStyle

    B --> G1["GRUPO 1"]:::g1Style
    B --> G2["GRUPO 2"]:::g2Style
    B --> G3["GRUPO 3"]:::g3Style

    B --> C["CONCLUSION GENERAL<br/>Los Grupos 2 y 3 confirman una relacion fuerte y confiable entre estudio y calificaciones.<br/>El Grupo 1 no muestra relacion lineal."]:::concStyle

    G1 --> G1_1["Ecuacion: y = 85.31 - 0.1061x<br/>r = -0.0571<br/>p = 0.69<br/>R² = 0.0033"]:::detailStyle

    G2 --> G2_1["Ecuacion: y = 15.30 + 4.2227x<br/>r = 0.8620<br/>p < 0.05<br/>R² = 0.7430"]:::detailStyle

    G3 --> G3_1["Ecuacion: y = 0.10 + 5.2857x<br/>r = 0.9422<br/>p < 0.05<br/>R² = 0.8878"]:::detailStyle
```

---

<a id="graficas"></a>

##  4. Visualización Gráfica de los Modelos

### 🔹 Análisis Detallado del Grupo 1

- **Comportamiento:** No muestra una relación lineal perceptible ($r = -0.0571$). El valor de $p$ es mayor a $0.05$, lo que indica que el modelo no es estadísticamente significativo ni confiable ($R^2 = 0.0033$).

<p align="center">
<img src="Graficas/graficas_grupo_1.png" width="850">
</p>

### 🔹 Análisis Detallado del Grupo 2

- **Comportamiento:** Presenta una correlación fuerte y positiva ($r = 0.8620$). El modelo es confiable y explica el 74.30% de la variabilidad de las calificaciones ($R^2 = 0.7430$).

<p align="center">
<img src="Graficas/graficas_grupo_2.png" width="850">
</p>

### 🔹 Análisis Detallado del Grupo 3

- **Comportamiento:** Muestra una correlación positiva casi perfecta ($r = 0.9422$). Es el modelo más sólido de los tres, con un ajuste lineal excelente ($R^2 = 0.8878$).

<p align="center">
<img src="Graficas/graficas_grupo_3.png" width="850">
</p>

---

<a id="conclusion"></a>

##  5. Conclusión General

Los análisis realizados en los **Grupos 2 y 3** confirman de manera empírica que existe una relación directa, fuerte y estadísticamente confiable entre las horas de estudio y las calificaciones obtenidas. Por el contrario, el comportamiento observado en el **Grupo 1** sugiere la presencia de factores externos que impiden modelar linealmente el rendimiento académico.

---

<a id="repositorio"></a>

## 🛠️ 6. Estructura del Repositorio y Accesos Directos

###  Datos

-  [grupo1.csv](Datos/grupo1.csv)
-  [grupo2.csv](Datos/grupo2.csv)
-  [grupo3.csv](Datos/grupo3.csv)

###  Código

- 🐍 [Practica_Regresion.py](Codigo/Practica_Regresion.py)

###  Gráficas

-  [graficas_grupo_1.png](Graficas/graficas_grupo_1.png)
-  [graficas_grupo_2.png](Graficas/graficas_grupo_2.png)
-  [graficas_grupo_3.png](Graficas/graficas_grupo_3.png)

###  Documentación

-  [README.md](README.md)
-  [EJECUCION_GITHUB_ACTIONS.md](Codigo/EJECUCION_GITHUB_ACTIONS.md)
Prueba GitHub Actions.
