import pandas as pd # Importa la biblioteca Pandas, esencial para la manipulación y análisis de datos en formato tabular.

# --- 1. Cargar el dataset desde la URL ---
# Define la dirección web donde se encuentra el archivo CSV.
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'
try:
    # Intenta leer el archivo CSV en un DataFrame.
    # El parámetro 'sep=';'' indica que los valores en el archivo están separados por punto y coma.
    inmuebles = pd.read_csv(url, sep=';')
    print("Dataset cargado exitosamente.")
except Exception as e:
    # Si ocurre un error al cargar el dataset (ej. problema de red), lo imprime y sale.
    print(f"Error al cargar el dataset desde la URL: {e}")
    print("Por favor, verifica la URL o tu conexión a internet e intenta de nuevo.")
    exit() # Sale del script si no se puede cargar el dataset.


# --- 2. Exploración inicial del DataFrame (antes de la imputación) ---
# Muestra un resumen conciso del DataFrame para identificar columnas con valores nulos (NaN)
# y verificar sus tipos de datos. Esto es crucial antes de decidir cómo imputar.
print("\n--- Información General del DataFrame (antes de la imputación) ---")
print(inmuebles.info())

# --- 3. Rellenar valores nulos (NaN) con la media (promedio) de sus columnas ---
# Identificamos las columnas numéricas que suelen tener valores faltantes en este dataset
# y para las cuales rellenar con la media es una estrategia común (imputación).
# Las columnas 'Valor', 'Condominio' e 'Impuesto' se identifican con frecuencia como tener nulos.

# Calcula la media de cada una de estas columnas.
# .mean() calcula el promedio de todos los valores no nulos en la Serie (columna).
mean_valor = inmuebles['Valor'].mean()
mean_condominio = inmuebles['Condominio'].mean()
mean_impuesto = inmuebles['Impuesto'].mean()

# Rellena los valores nulos (NaN) en las columnas específicas con las medias calculadas.
# .fillna() es el método de Pandas para reemplazar valores faltantes.
# 'inplace=True' modifica el DataFrame original directamente, lo cual es eficiente para grandes DataFrames.
inmuebles['Valor'].fillna(mean_valor, inplace=True)
inmuebles['Condominio'].fillna(mean_condominio, inplace=True)
inmuebles['Impuesto'].fillna(mean_impuesto, inplace=True)

# --- 4. Verificación de la imputación ---
# Mostramos la información del DataFrame nuevamente para confirmar que los valores nulos
# en las columnas imputadas han sido rellenados (su 'Non-Null Count' ahora debería ser igual al total de entradas).
print("\n--- Información General del DataFrame (después de la imputación) ---")
print(inmuebles.info())

# --- 5. Análisis y clasificación de la columna 'Impuesto' (con valores imputados) ---
# Ahora que la columna 'Impuesto' no tiene valores nulos, podemos realizar el análisis completo.

# Ordena el DataFrame completo por la columna 'Impuesto' en orden descendente.
# Esto coloca las propiedades con los impuestos más altos al principio del DataFrame.
# 'ascending=False' garantiza el orden de mayor a menor.
impuestos_mas_altos_ordenados = inmuebles.sort_values(by='Impuesto', ascending=False)

# Muestra las 10 propiedades con los impuestos más altos.
# .head(10) selecciona las primeras 10 filas del DataFrame ya ordenado,
# que corresponden a las propiedades con los impuestos más elevados.
print("\n--- Propiedades con los Impuestos Más Altos (Top 10) después de imputación ---")
print(impuestos_mas_altos_ordenados.head(10))
