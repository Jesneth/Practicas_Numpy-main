# Análisis Exploratorio de Datos de Alquileres con Pandas

Este repositorio contiene tres scripts de Python diseñados para realizar un análisis exploratorio de un conjunto de datos de alquileres utilizando la biblioteca Pandas. Cada script se enfoca en responder preguntas específicas sobre los datos, aplicando diversas funcionalidades de Pandas para limpiar, manipular, analizar y visualizar la información.

## Descripción del Dataset

El dataset utilizado en estos scripts se carga desde un archivo CSV ubicado en la siguiente URL:

https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv

Este archivo contiene información sobre diferentes propiedades en alquiler, incluyendo características como el tipo de propiedad, el barrio, la cantidad de habitaciones, la cantidad de baños y el valor del alquiler. Los scripts exploran diversas relaciones y distribuciones dentro de estos datos.

## Scripts Incluidos

1.  **`practica_1_analisis_por_barrio.py`**: Este script se enfoca en analizar los datos de alquileres agrupados por barrio.

    **Pasos Realizados:**

    * **Carga de Datos:** Se carga el archivo CSV en un DataFrame de Pandas.
    * **Exploración Inicial (Opcional):** Se muestra información básica del DataFrame para entender su estructura.
    * **Cálculo de Promedios por Barrio:** Se calcula el precio de alquiler promedio, la cantidad promedio de habitaciones y la cantidad promedio de baños para cada barrio utilizando la función `groupby()` y `.mean()`.
    * **Identificación de Barrios con Alquileres Extremos:** Se identifican el barrio con el precio de alquiler promedio más alto y el más bajo, utilizando `sort_values()` e `.iloc[]`.
    * **Conteo de Propiedades por Tipo en Cada Barrio:** Se determina la cantidad de propiedades de cada tipo (casa, apartamento, etc.) en cada barrio utilizando `groupby()`, `.size()` y `.unstack()` para una mejor visualización.
    * **Visualización de los Barrios Más Caros:** Se crea un gráfico de barras horizontales mostrando el precio de alquiler promedio de los 10 barrios más caros, utilizando `.plot(kind='bar')` de Matplotlib.
    * **Análisis Detallado de un Barrio Específico:** Se utiliza la función `query()` para seleccionar las propiedades de un barrio específico y se muestran estadísticas descriptivas (media, desviación estándar, etc.) de las columnas numéricas relevantes utilizando `.describe()`.

2.  **`practica_2_exploracion_caracteristicas.py`**: Este script explora la relación entre diferentes características de las propiedades y el valor del alquiler.

    **Pasos Realizados:**

    * **Carga de Datos:** Se carga el archivo CSV en un DataFrame de Pandas.
    * **Cálculo de Correlación:** Se calcula la correlación entre el número de habitaciones y el valor del alquiler utilizando `.corr()` para entender si existe una relación lineal entre estas variables.
    * **Análisis del Alquiler Promedio por Número de Habitaciones:** Se agrupan los datos por la cantidad de habitaciones y se calcula el valor del alquiler promedio para cada grupo utilizando `groupby()` y `.mean()`.
    * **Análisis del Alquiler Promedio por Número de Baños:** Se realiza el mismo análisis que el paso anterior, pero utilizando la cantidad de baños como criterio de agrupación.
    * **Visualización de Distribuciones:** Se crean histogramas para visualizar la distribución del número de habitaciones, la cantidad de baños y el valor del alquiler utilizando `.hist()` de Matplotlib.
    * **Filtrado por Múltiples Condiciones:** Se utiliza la función `query()` para seleccionar propiedades que cumplen con múltiples criterios (por ejemplo, más de 3 habitaciones y un alquiler inferior a un cierto valor).

3.  **`practica_3_comparacion_tipos_residenciales.py`**: Este script se centra en comparar las características y precios de diferentes tipos de inmuebles residenciales.

    **Pasos Realizados:**

    * **Carga de Datos:** Se carga el archivo CSV en un DataFrame de Pandas.
    * **Filtrado de Inmuebles Residenciales:** Se define una lista de tipos de inmuebles comerciales y se utiliza `query()` para filtrar el DataFrame,保留ando solo los tipos de inmuebles residenciales.
    * **Cálculo del Alquiler Promedio por Tipo Residencial:** Se calcula el valor del alquiler promedio para cada tipo de inmueble residencial utilizando `groupby()` y `.mean()`.
    * **Cálculo de Características Promedio por Tipo Residencial:** Se determina la cantidad promedio de habitaciones y baños para cada tipo de inmueble residencial utilizando `groupby()` y `.mean()` en múltiples columnas.
    * **Visualización de la Comparativa de Alquileres:** Se crea un gráfico de barras horizontales comparando el valor del alquiler promedio entre los diferentes tipos de inmuebles residenciales utilizando `.plot(kind='barh')` de Matplotlib.
    * **Cálculo de Múltiples Estadísticas por Tipo Residencial:** Se utiliza la función `.agg()` después de `groupby()` para calcular múltiples estadísticas descriptivas (media, mediana, desviación estándar, mínimo, máximo y conteo) del valor del alquiler para cada tipo de inmueble residencial.

## Cómo Utilizar

Para ejecutar estos scripts, asegúrate de tener instaladas las bibliotecas Pandas y Matplotlib en tu entorno de Python. Puedes instalarlas utilizando pip:

```bash
pip install pandas matplotlib
```
Aprendizaje

Estos scripts demuestran varios conceptos fundamentales de Pandas para el análisis exploratorio de datos, incluyendo:

    Carga de datos desde archivos CSV (pd.read_csv()).
    Exploración básica de DataFrames (.head(), .info(), .describe()).
    Selección de columnas.
    Filtrado de filas utilizando condiciones (query()).
    Agrupación de datos (groupby()).
    Cálculo de estadísticas agregadas (.mean(), .size(), .agg()).
    Ordenamiento de DataFrames (sort_values()).
    Transformación de la estructura de datos (unstack()).
    Visualización de datos utilizando gráficos de barras e histogramas (.plot(), .hist() de Matplotlib).
    Interpretación de correlaciones.

# Funciones y Métodos de Pandas y Matplotlib Utilizados

## Funciones y Métodos de Pandas:

* **`pd.read_csv(url, sep=';')`**:
    * **Función:** Lee datos desde un archivo CSV (Comma Separated Values) y los carga en un DataFrame de Pandas.
    * **Parámetros:**
        * `url`: La dirección web (URL) o la ruta local del archivo CSV.
        * `sep=';'`: Especifica el delimitador de campos en el archivo CSV. En este caso, los valores están separados por un punto y coma (;). Si fuera una coma, usaríamos `sep=','`.
    * **Qué hace en el código:** Carga el dataset de alquileres desde la URL proporcionada, creando la estructura tabular (DataFrame) con la que trabajaremos.

* **`.head()`**:
    * **Método de DataFrame:** Muestra las primeras `n` filas del DataFrame. Por defecto, muestra las primeras 5 filas.
    * **Qué hace en el código:** Permite obtener una vista rápida de la estructura y los primeros datos del DataFrame cargado, ayudando a entender las columnas y los tipos de datos.

* **`.info()`**:
    * **Método de DataFrame:** Proporciona un resumen conciso del DataFrame, incluyendo el número total de filas, el número de columnas, los nombres de las columnas, el tipo de datos de cada columna y la cantidad de valores no nulos en cada una. También informa sobre el uso de memoria del DataFrame.
    * **Qué hace en el código:** Ofrece una visión general de la calidad y la estructura del DataFrame, útil para identificar posibles problemas como tipos de datos incorrectos o valores faltantes.

* **`.describe()`**:
    * **Método de DataFrame:** Genera estadísticas descriptivas de las columnas numéricas del DataFrame. Estas estadísticas incluyen el conteo, la media, la desviación estándar, el mínimo, el máximo y los percentiles (25%, 50%, 75%).
    * **Qué hace en el código:** Proporciona un resumen estadístico de las variables numéricas, ayudando a entender su distribución y a identificar posibles valores atípicos.

* **`[['Nombre_Columna1', 'Nombre_Columna2']]` (Selección de Columnas)**:
    * **Operador de DataFrame:** Se utiliza para seleccionar una o más columnas del DataFrame. Pasar una lista de nombres de columnas (dentro de doble corchete) devuelve un nuevo DataFrame que contiene solo esas columnas.
    * **Qué hace en el código:** Se utiliza para enfocar el análisis en columnas específicas, por ejemplo, al calcular la correlación entre 'Habitaciones' y 'Valor'.

* **`.corr()`**:
    * **Método de DataFrame:** Calcula la matriz de correlación por pares de todas las columnas numéricas en el DataFrame. La correlación mide la fuerza y la dirección de una relación lineal entre dos variables. Los valores varían de -1 (correlación negativa perfecta) a 1 (correlación positiva perfecta), con 0 indicando ninguna correlación lineal.
    * **Qué hace en el código:** En la Práctica 2, se usa para cuantificar la relación lineal entre el número de habitaciones y el valor del alquiler.

* **`.groupby('Nombre_Columna')`**:
    * **Método de DataFrame:** Agrupa las filas del DataFrame basándose en los valores únicos de la columna especificada ('Nombre\_Columna'). Esto crea objetos de grupo que luego se pueden usar para realizar cálculos agregados en cada grupo.
    * **Qué hace en el código:** Se utiliza extensivamente para realizar análisis por categorías, como calcular el promedio del alquiler por barrio o por tipo de inmueble.

* **`.mean()`**:
    * **Método de Series o DataFrameGroupBy:** Calcula la media (promedio) de los valores. Cuando se aplica a un objeto `DataFrameGroupBy`, se calcula la media de cada columna numérica dentro de cada grupo.
    * **Qué hace en el código:** Se usa para encontrar el valor promedio del alquiler, el número promedio de habitaciones y el número promedio de baños por diferentes grupos (barrio, tipo de inmueble, número de habitaciones, etc.).

* **`.sort_values('Nombre_Columna', ascending=False)`**:
    * **Método de DataFrame:** Ordena las filas del DataFrame según los valores de la columna especificada ('Nombre\_Columna').
    * **Parámetros:**
        * `by='Nombre_Columna'`: Especifica la columna por la cual ordenar.
        * `ascending=False`: Indica si la ordenación debe ser descendente (de mayor a menor). Si fuera `True` (valor por defecto), la ordenación sería ascendente.
    * **Qué hace en el código:** Se utiliza para encontrar los barrios con los alquileres más altos o más bajos, o para ordenar los resultados de los agrupamientos para una mejor interpretación.

* **`.iloc[0]`**:
    * **Atributo de DataFrame o Series:** Permite la selección basada en la posición entera (índice) de las filas y columnas. `.iloc[0]` selecciona la primera fila (índice 0).
    * **Qué hace en el código:** Después de ordenar los DataFrames por el promedio del alquiler, `.iloc[0]` se usa para seleccionar la fila que contiene el barrio con el valor más alto o más bajo.

* **`.size()`**:
    * **Método de DataFrameGroupBy:** Devuelve una Serie que contiene el tamaño de cada grupo. Cuando se agrupa por múltiples columnas, el resultado es una Serie con un índice jerárquico.
    * **Qué hace en el código:** En la Práctica 1, después de agrupar por 'Barrio' y 'Tipo', `.size()` cuenta cuántas propiedades de cada tipo hay en cada barrio.

* **`.unstack(fill_value=0)`**:
    * **Método de Series o DataFrame:** Pivota un nivel del índice (generalmente el más interno) de una Serie o DataFrame al convertirse en nombres de columna.
    * **Parámetros:**
        * `fill_value=0`: Reemplaza los valores faltantes (NaN) que resultan del unstacking con el valor especificado (en este caso, 0).
    * **Qué hace en el código:** Transforma la Serie resultante de `groupby(['Barrio', 'Tipo']).size()` para que los tipos de inmueble se conviertan en columnas, facilitando la visualización de la cantidad de cada tipo por barrio.

* **`.query('condición')`**:
    * **Método de DataFrame:** Filtra el DataFrame basándose en una expresión de consulta. La sintaxis de la consulta es similar a SQL. Se pueden usar variables Python dentro de la consulta precediéndolas con `@`.
    * **Qué hace en el código:** Se utiliza para seleccionar filas que cumplen con ciertos criterios, como propiedades en un barrio específico, propiedades con más de cierto número de habitaciones y un alquiler por debajo de un límite, o para excluir tipos de inmuebles comerciales.

* **`.hist(bins=..., edgecolor='black')`**:
    * **Método de Series:** Genera un histograma de los valores en la Serie. Un histograma es una representación gráfica de la distribución de datos numéricos, donde los datos se agrupan en "bins" y la altura de cada barra representa la frecuencia de los valores en ese bin.
    * **Parámetros:**
        * `bins`: Especifica el número de bins (barras) en el histograma o los límites de los bins.
        * `edgecolor='black'`: Establece el color del borde de las barras.
    * **Qué hace en el código:** Permite visualizar la distribución de variables numéricas como el número de habitaciones, baños y el valor del alquiler.

* **`.agg(['mean', 'median', 'std', 'min', 'max', 'count'])`**:
    * **Método de DataFrameGroupBy:** Aplica una o más funciones de agregación a las columnas especificadas para cada grupo.
    * **Parámetro:** Una lista de nombres de funciones de agregación (como `'mean'`, `'median'`, `'std'` - desviación estándar, `'min'`, `'max'`, `'count'` - número de elementos).
    * **Qué hace en el código:** Permite calcular múltiples estadísticas descriptivas (promedio, valor central, dispersión, extremos y cantidad) para el valor del alquiler dentro de cada tipo de inmueble residencial.

* **`.value_counts(normalize=True)`**:
    * **Método de Series:** Devuelve una Serie que contiene los conteos de valores únicos en la Serie.
    * **Parámetro:**
        * `normalize=True`: Si se establece en `True`, en lugar de los conteos absolutos, devuelve la frecuencia relativa (proporción) de cada valor único.
    * **Qué hace en el código:** Se utiliza (aunque no en estas prácticas específicas) para obtener la distribución de categorías, como el porcentaje de cada tipo de inmueble en el dataset.

## Funciones y Métodos de Matplotlib (usados para visualización):

* **`import matplotlib.pyplot as plt`**:
    * **Importación:** Importa el módulo `pyplot` de la biblioteca Matplotlib y lo asigna al alias `plt`. Este módulo proporciona una interfaz similar a MATLAB para la creación de gráficos.

* **`plt.figure(figsize=(ancho, alto))`**:
    * **Función:** Crea una nueva figura para un gráfico. El parámetro `figsize` especifica el ancho y el alto de la figura en pulgadas.
    * **Qué hace en el código:** Se usa para controlar el tamaño de los gráficos generados.

* **`plt.subplot(filas, columnas, indice)`**:
    * **Función:** Añade un subplot (un área de trazado) a la figura actual. Los argumentos especifican el número de filas y columnas de la cuadrícula de subplots, y el índice del subplot que se va a crear (empezando desde 1, llenando por filas).
    * **Qué hace en el código:** En la Práctica 2, se utiliza para crear una figura con tres subplots para mostrar los histogramas de diferentes variables en la misma imagen.

* **`.plot(kind='bar', ...)` y `.plot(kind='barh', ...)` (Método de Series o DataFrame):**
    * **Método:** Genera diferentes tipos de gráficos basados en los datos de una Serie o DataFrame. El parámetro `kind` especifica el tipo de gráfico.
    * **Parámetros relevantes:**
        * `kind='bar'`: Crea un gráfico de barras verticales.
        * `kind='barh'`: Crea un gráfico de barras horizontales.
        * `figsize`: Tamaño de la figura.
        * `color`: Color de las barras.
    * **Qué hace en el código:** Se utiliza para visualizar comparaciones entre categorías (como el precio promedio por barrio o por tipo de inmueble).

* **`plt.title('Título del Gráfico')`**:
    * **Función:** Establece el título del gráfico actual.

* **`plt.xlabel('Etiqueta del Eje X')`**:
    * **Función:** Establece la etiqueta del eje x del gráfico actual.

* **`plt.ylabel('Etiqueta del Eje Y')`**:
    * **Función:** Establece la etiqueta del eje y del gráfico actual.

* **`plt.xticks(rotation=ángulo, ha='alineación')`**:
    * **Función:** Establece las etiquetas y propiedades de las marcas del eje x.
    * **Parámetros:**
        * `rotation`: Ángulo de rotación de las etiquetas en grados.
        * `ha`: Alineación horizontal de las etiquetas (`'right'`, `'center'`, `'left'`).
    * **Qué hace en el código:** Se usa para rotar las etiquetas del eje x en el gráfico de barras de los barrios para evitar que se superpongan.

* **`plt.tight_layout()`**:
    * **Función:** Ajusta automáticamente el espaciado entre los subplots para evitar que las etiquetas se superpongan.

* **`plt.show()`**:
    * **Función:** Muestra el gráfico que se ha creado.