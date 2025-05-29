
# 1. Instalacón de la biblioteca pandas 
# Importación de la biblioteca, junto con su alias ya que éste es el que nos va a permitir el análisis de datos tabulares 
import pandas as pd 

# Carga la DB desde la URL y la almaceno en una variable llamada "url"
url = 'https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv'

# Se realiza lectura del archivo por medio del metódo ".read_csv()" ya instalado en pandas e ingresando como parámetro la url.
inmuebles = pd.read_csv(url, sep=';')
# Los datos leidos se almacenan en un DataFrame llamado "inmuebles"
# El uso de "sep=';'" es para que separe la informacián con un punto y coma. 


# Imprimir el promedio de los impuestos más altos del DataFrame "Inmuebles"
impuestos = inmuebles.groupby('Tipo')['Impuesto'].mean()

# Ordenar de forma ascendente
impuestos_ordenados = impuestos.sort_values(ascending=False)


print(impuestos_ordenados)


