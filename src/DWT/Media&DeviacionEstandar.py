import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('results/distancias_euclidianas.csv')

# Extraer la columna de distancias
distancias = data['Distancia Euclidiana']

# Calcular media y desviación estándar
media = distancias.mean()
desviacion_estandar = distancias.std()

print(f"Media: {media}")
print(f"Desviación estándar: {desviacion_estandar}")