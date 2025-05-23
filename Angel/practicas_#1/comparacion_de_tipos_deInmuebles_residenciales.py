import pandas as pd
import matplotlib.pyplot as plt

# 1. Carga los datos desde la URL
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
inmuebles = pd.read_csv(url, sep=';')
print("Primeras filas de inmuebles residenciales:\n", inmuebles.head())

# 2. Define la lista de inmuebles comerciales para poder filtrar los residenciales
inmuebles_comerciales = ['Conjunto Comercial/Sala', 'Edificio Completo', 'Tienda/Salón', 'Casa Comercial',
                        'Terreno Estándar', 'Cochera/Estacionamiento', 'Galpón/Depósito/Almacén',
                        'Tienda en Centro Comercial', 'Hotel', 'Loteo/Condominio', 'Industria']

# 3. Filtra el DataFrame para incluir solo los tipos de inmuebles que NO están en la lista de comerciales
inmuebles_residenciales = inmuebles.query('Tipo not in @inmuebles_comerciales')
print("\nPrimeras filas de inmuebles residenciales:\n", inmuebles_residenciales.head())

# 4. Calcula el valor del alquiler promedio por tipo de inmueble residencial
promedio_alquiler_por_tipo_residencial = inmuebles_residenciales.groupby('Tipo')['Valor'].mean().sort_values()
# Agrupa el DataFrame 'inmuebles_residenciales' por la columna 'Tipo'.
# Luego, selecciona la columna 'Valor' y calcula la media (promedio) para cada tipo.
# Finalmente, ordena los resultados por el valor promedio del alquiler de forma ascendente.
print("\nValor del alquiler promedio por tipo de inmueble residencial:\n", promedio_alquiler_por_tipo_residencial)

# 5. Determina la cantidad promedio de habitaciones y suites por tipo de inmueble residencial
# Nota: Se usó 'Suites' en lugar de 'Banos' ya que la columna 'Banos' no se encontró en el DataFrame.
promedio_caracteristicas_por_tipo = inmuebles_residenciales.groupby('Tipo')[['Habitaciones', 'Suites']].mean()
# Agrupa el DataFrame 'inmuebles_residenciales' por la columna 'Tipo'.
# Luego, selecciona las columnas 'Habitaciones' y 'Suites' y calcula la media (promedio) para cada tipo.
print("\nPromedio de habitaciones y suites por tipo de inmueble residencial:\n", promedio_caracteristicas_por_tipo)

# 6. Crea un gráfico de barras horizontales comparando el valor del alquiler promedio por tipo de inmueble residencial
promedio_alquiler_por_tipo_residencial.plot(kind='barh', figsize=(10, 6), color='lightcoral')
# Utiliza el método 'plot()' para crear un gráfico de barras horizontales ('barh').
# 'figsize' establece el tamaño de la figura.
# 'color' establece el color de las barras.
plt.title('Valor del Alquiler Promedio por Tipo de Inmueble Residencial')
# Establece el título del gráfico.
plt.xlabel('Valor Promedio')
# Establece la etiqueta del eje x.
plt.ylabel('Tipo de Inmueble')
# Establece la etiqueta del eje y.
plt.tight_layout()
# Ajusta el diseño para evitar que las etiquetas se superpongan.
plt.show()
# Muestra el gráfico.

# 7. Utiliza groupby() y agg() para calcular múltiples estadísticas del valor del alquiler por tipo de inmueble residencial
estadisticas_alquiler_por_tipo = inmuebles_residenciales.groupby('Tipo')['Valor'].agg(['mean', 'median', 'std', 'min', 'max', 'count'])
# Agrupa el DataFrame 'inmuebles_residenciales' por la columna 'Tipo'.
# Luego, selecciona la columna 'Valor' y aplica la función de agregación 'agg()'.
# 'agg()' permite calcular múltiples estadísticas (media, mediana, desviación estándar, mínimo, máximo y conteo)
# para cada grupo (tipo de inmueble) en una sola operación.
print("\nEstadísticas del valor del alquiler por tipo de inmueble residencial:\n", estadisticas_alquiler_por_tipo)