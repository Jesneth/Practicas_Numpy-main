import pandas as pd # Importa la biblioteca Pandas, que es fundamental para el análisis de datos tabulares. Se le asigna el alias 'pd' para facilitar su uso.
import matplotlib.pyplot as plt # Importa la biblioteca Matplotlib, específicamente el módulo 'pyplot', que se utiliza para crear gráficos. Se le asigna el alias 'plt'.

# 1. Carga los datos desde la URL
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
# Define la URL del archivo CSV que contiene los datos de alquileres.
inmuebles = pd.read_csv(url, sep=';')
# Utiliza la función 'read_csv' de Pandas para leer el archivo desde la URL.
# El parámetro 'sep=';' indica que los valores dentro del archivo están separados por un punto y coma.
# Los datos leídos se almacenan en un DataFrame llamado 'inmuebles'.
print("Primeras filas del DataFrame:\n", inmuebles.head())
# Muestra las primeras filas del DataFrame 'inmuebles' utilizando el método 'head()'.
# Esto permite inspeccionar rápidamente la estructura de los datos y los nombres de las columnas.

# 2. Explora los datos (opcional, pero recomendado para recordar la estructura)
print("\nInformación general del DataFrame:\n", inmuebles.info())
# Utiliza el método 'info()' para obtener un resumen del DataFrame.
# Esto incluye el número de filas, el número de columnas, los tipos de datos de cada columna
# y la cantidad de valores no nulos. Es útil para entender la integridad de los datos.

# 3. Calcula el precio de alquiler promedio, habitaciones promedio y suites promedio por colonia
promedio_por_colonia = inmuebles.groupby('Colonia')[['Valor', 'Habitaciones', 'Suites']].mean()
# Utiliza el método 'groupby('Colonia')' para agrupar el DataFrame 'inmuebles' según los valores únicos de la columna 'Colonia'.
# Esto crea un objeto GroupBy donde cada grupo representa una colonia diferente.
# Luego, se seleccionan las columnas 'Valor', 'Habitaciones' y 'Suites' dentro de cada grupo.
# Finalmente, se aplica el método 'mean()' para calcular el promedio de estos valores para cada colonia.
# El resultado es un nuevo DataFrame llamado 'promedio_por_colonia', donde el índice son las colonias
# y las columnas son el promedio del valor, las habitaciones y las suites.
print("\nPromedio de alquiler, habitaciones y suites por colonia:\n", promedio_por_colonia)
# Muestra el DataFrame 'promedio_por_colonia' que contiene los promedios calculados por colonia.

# 4. Identifica la colonia con el alquiler promedio más alto y más bajo
colonia_mayor_promedio = promedio_por_colonia.sort_values('Valor', ascending=False).iloc[0]
# Utiliza el método 'sort_values('Valor', ascending=False)' para ordenar el DataFrame 'promedio_por_colonia'
# según la columna 'Valor' de forma descendente (el valor más alto primero).
# Luego, se utiliza '.iloc[0]' para seleccionar la primera fila del DataFrame ordenado,
# que corresponde a la colonia con el precio de alquiler promedio más alto.
colonia_menor_promedio = promedio_por_colonia.sort_values('Valor', ascending=True).iloc[0]
# Similar al paso anterior, pero 'ascending=True' ordena de forma ascendente (el valor más bajo primero),
# y '.iloc[0]' selecciona la primera fila, que es la colonia con el precio de alquiler promedio más bajo.
print("\nColonia con el alquiler promedio más alto:\n", colonia_mayor_promedio)
print("\nColonia con el alquiler promedio más bajo:\n", colonia_menor_promedio)

# 5. Determina la cantidad de propiedades de cada tipo en cada colonia
cantidad_por_tipo_colonia = inmuebles.groupby(['Colonia', 'Tipo']).size().unstack(fill_value=0)
# Utiliza 'groupby(['Colonia', 'Tipo'])' para agrupar el DataFrame por dos columnas: primero por 'Colonia'
# y luego, dentro de cada colonia, por 'Tipo' de inmueble.
# El método 'size()' calcula el número de filas (propiedades) en cada combinación única de colonia y tipo.
# El método 'unstack(fill_value=0)' pivota la tabla resultante, moviendo los valores únicos de la columna 'Tipo'
# al nivel de las columnas. Los valores que no tienen una combinación correspondiente se rellenan con 0 gracias a 'fill_value=0'.
# El resultado es un DataFrame donde las filas son las colonias y las columnas son los tipos de inmueble,
# con los valores indicando la cantidad de cada tipo en cada colonia.
print("\nCantidad de propiedades por tipo en cada colonia:\n", cantidad_por_tipo_colonia)

# 6. Crea un gráfico de barras del precio de alquiler promedio para las 10 colonias más caras
promedio_top_10_colonias = promedio_por_colonia.sort_values('Valor', ascending=False).head(10)
# Ordena el DataFrame 'promedio_por_colonia' por la columna 'Valor' de forma descendente
# y utiliza 'head(10)' para seleccionar las 10 colonias con el precio de alquiler promedio más alto.
promedio_top_10_colonias['Valor'].plot(kind='bar', figsize=(12, 6), color='skyblue')
# Utiliza el método 'plot()' para crear un gráfico de barras.
# 'kind='bar'' especifica el tipo de gráfico como barras verticales.
# 'figsize=(12, 6)' establece el tamaño de la figura (ancho=12 pulgadas, alto=6 pulgadas).
# 'color='skyblue'' establece el color de las barras.
plt.title('Precio de Alquiler Promedio para las 10 Colonias Más Caras')
# Establece el título del gráfico utilizando la función 'title()' de Matplotlib.
plt.xlabel('Colonia')
# Establece la etiqueta del eje x utilizando la función 'xlabel()' de Matplotlib.
plt.ylabel('Precio Promedio')
# Establece la etiqueta del eje y utilizando la función 'ylabel()' de Matplotlib.
plt.xticks(rotation=45, ha='right')
# Utiliza 'xticks()' para rotar las etiquetas del eje x en 45 grados ('rotation=45')
# y alinear el texto a la derecha ('ha='right'') para evitar que se superpongan.
plt.tight_layout()
# Ajusta automáticamente el espaciado entre los elementos del gráfico para evitar recortes.
plt.show()
# Muestra el gráfico creado utilizando la función 'show()' de Matplotlib.

# 7. Selecciona propiedades en una colonia específica y muestra estadísticas descriptivas
colonia_seleccionada = 'Polanco' # Elige la colonia que quieras analizar
# Define el nombre de la colonia que se utilizará para el análisis detallado.
propiedades_colonia = inmuebles.query('Colonia == @colonia_seleccionada')
# Utiliza el método 'query()' para filtrar el DataFrame 'inmuebles' y seleccionar solo las filas
# donde el valor de la columna 'Colonia' es igual al valor de la variable 'colonia_seleccionada'.
# El '@' antes del nombre de la variable permite referenciar variables Python dentro de la consulta.
print(f"\nPropiedades en la colonia de {colonia_seleccionada}:\n", propiedades_colonia.head())
# Muestra las primeras filas del DataFrame filtrado que contiene solo las propiedades de la colonia seleccionada.

estadisticas_colonia = propiedades_colonia[['Valor', 'Habitaciones', 'Suites']].describe()
# Selecciona las columnas 'Valor', 'Habitaciones' y 'Suites' del DataFrame filtrado
# y utiliza el método 'describe()' para generar estadísticas descriptivas de estas columnas.
# Esto incluye la media, la desviación estándar, el mínimo, el máximo, los cuartiles, etc.
print(f"\nEstadísticas descriptivas de las propiedades en {colonia_seleccionada}:\n", estadisticas_colonia)
# Muestra las estadísticas descriptivas de las propiedades en la colonia seleccionada.