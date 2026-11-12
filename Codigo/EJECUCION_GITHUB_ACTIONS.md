# Ejecución del Proyecto desde GitHub

## Descripción

Este proyecto incluye una automatización mediante **GitHub Actions** que permite ejecutar el programa de Python directamente en los servidores de GitHub sin necesidad de instalar Python, Pandas, Matplotlib, SciPy o Scikit-Learn en el equipo local.

El flujo automatizado realiza las siguientes tareas:

1. Descarga el repositorio.
2. Instala Python y las dependencias necesarias.
3. Ejecuta el archivo:

```text
Codigo/Practica_Regresion.py
```

4. Genera automáticamente las gráficas:

```text
Graficas/graficas_grupo_1.png
Graficas/graficas_grupo_2.png
Graficas/graficas_grupo_3.png
```

5. Actualiza los resultados en el repositorio.

---

# ▶ Ejecución Manual desde GitHub

## Paso 1

Ingresar al repositorio en GitHub.

## Paso 2

Seleccionar la pestaña:

```text
Actions
```

## Paso 3

Elegir el flujo de trabajo:

```text
Ejecutar Script y Actualizar Graficas
```

## Paso 4

Pulsar el botón:

```text
Run workflow
```

ubicado en la esquina superior derecha.

## Paso 5

Confirmar nuevamente:

```text
Run workflow
```

GitHub comenzará a ejecutar el programa automáticamente en sus servidores.

---

#  Verificación de Resultados

Una vez finalizada la ejecución:

1. Regresar a la pestaña:

```text
Code
```

2. Abrir la carpeta:

```text
Graficas
```

3. Verificar la actualización de:

```text
graficas_grupo_1.png
graficas_grupo_2.png
graficas_grupo_3.png
```

---

#  Visualización de la Consola

Para visualizar la ejecución del programa:

```text
Actions
→ Ejecutar Script y Actualizar Graficas
→ run-python-script
→ Ejecutar Script
```

En esta sección podrá observarse la salida generada por:

```python
python Codigo/Practica_Regresion.py
```

incluyendo:

- Estadísticas descriptivas.
- Regresión lineal.
- Correlación de Pearson.
- Valores de R².
- Generación de gráficas.

---

#  Archivo de Configuración

La automatización está definida mediante:

```text
.github/workflows/run_script.yml
```

Mientras este archivo permanezca en el repositorio, el flujo podrá ejecutarse desde GitHub en cualquier momento.
