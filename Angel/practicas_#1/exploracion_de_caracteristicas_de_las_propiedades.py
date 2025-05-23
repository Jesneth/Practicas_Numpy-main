import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga los datos
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
inmuebles = pd.read_csv(url, sep=';')

# 2. Calcula la correlación entre el número de habitaciones y el valor del alquiler
#    - `.corr()`: Calcula la matriz de correlación por pares de todas las columnas numéricas en el DataFrame.
correlacion_habitaciones_valor = inmuebles[['Habitaciones', 'Valor']].corr()
#    - `[['Habitaciones', 'Valor']]`: Selecciona solo las dos columnas de interés antes de calcular la correlación.
print("\nCorrelación entre Habitaciones y Valor:\n", correlacion_habitaciones_valor)
#    - La correlación es un valor entre -1 y 1 que indica la fuerza y la dirección de la relación lineal entre dos variables.
#      Un valor cercano a 1 indica una correlación positiva fuerte (a medida que una variable aumenta, la otra también tiende a aumentar).
#      Un valor cercano a -1 indica una correlación negativa fuerte (a medida que una variable aumenta, la otra tiende a disminuir).
#      Un valor cercano a 0 indica una correlación débil o inexistente.

# 3. Agrupa por cantidad de habitaciones y calcula el valor del alquiler promedio
promedio_alquiler_por_habitacion = inmuebles.groupby('Habitaciones')['Valor'].mean().sort_index()
#    - `groupby('Habitaciones')`: Agrupa por la cantidad de habitaciones.
#    - `['Valor'].mean()`: Calcula el promedio del 'Valor' para cada grupo de habitaciones.
#    - `.sort_index()`: Ordena el resultado por el número de habitaciones (el índice).
print("\nValor del alquiler promedio por cantidad de habitaciones:\n", promedio_alquiler_por_habitacion)

# 4. Realiza el mismo análisis para la cantidad de baños
promedio_alquiler_por_bano = inmuebles.groupby('Suites')['Valor'].mean().sort_index()
print("\nValor del alquiler promedio por cantidad de baños:\n", promedio_alquiler_por_bano)

# 5. Crea histogramas para visualizar la distribución
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1) # Crea el primer subplot en una cuadrícula de 1 fila y 3 columnas
inmuebles['Habitaciones'].hist(bins=range(inmuebles['Habitaciones'].min(), inmuebles['Habitaciones'].max() + 2), edgecolor='black')
#    - `.hist()`: Crea un histograma.
#    - `bins=range(...)`: Define los bordes de las barras del histograma para que coincidan con los valores enteros de las habitaciones.
#    - `edgecolor='black'`: Añade bordes negros a las barras para mejor visualización.
plt.title('Distribución del Número de Habitaciones')
plt.xlabel('Número de Habitaciones')
plt.ylabel('Frecuencia')

plt.subplot(1, 3, 2) # Crea el segundo subplot
inmuebles['Suites'].hist(bins=range(inmuebles['Suites'].min(), inmuebles['Suites'].max() + 2), edgecolor='black')
plt.title('Distribución del Número de Baños')
plt.xlabel('Número de Baños')
plt.ylabel('Frecuencia')

plt.subplot(1, 3, 3) # Crea el tercer subplot
inmuebles['Valor'].hist(bins=20, edgecolor='black') # Puedes ajustar el número de 'bins' para cambiar la granularidad
plt.title('Distribución del Valor del Alquiler')
plt.xlabel('Valor del Alquiler')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# 6. Selecciona propiedades con más de 3 habitaciones y alquiler inferior a un valor
alquiler_maximo = 3000 # Establece un valor máximo de alquiler para el filtro
propiedades_filtradas = inmuebles.query('Habitaciones > 3 and Valor < @alquiler_maximo')
#    - `query('Habitaciones > 3 and Valor < @alquiler_maximo')`: Filtra las filas donde la columna 'Habitaciones'
#      es mayor que 3 Y (`and`) la columna 'Valor' es menor que el valor de la variable `alquiler_maximo`.
print(f"\nPropiedades con más de 3 habitaciones y alquiler menor a {alquiler_maximo}:\n", propiedades_filtradas.head())