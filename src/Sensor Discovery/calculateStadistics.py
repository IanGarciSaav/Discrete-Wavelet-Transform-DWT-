import pandas as pd
import numpy as np

# Ruta del archivo de firmas (signatures.csv)
input_file = "../../results/sensores/signatures.csv"
output_file = "../../results/sensores/statistics.csv"

# Cargar los datos
try:
    df = pd.read_csv(input_file)
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Verificar que la columna de coeficientes existe
if "Sensor" not in df.columns:
    print("Error: No se encontró la columna 'Sensor' en el archivo CSV.")
    exit()

# Obtener la lista de sensores únicos
sensors = df["Sensor"].unique()

# Lista para almacenar estadísticas
statistics = []

for sensor in sensors:
    sensor_data = df[df["Sensor"] == sensor].iloc[:, 1:]  # Excluir la columna "Sensor"
    
    # Calcular distancia euclidiana para cada fila respecto al centroide
    centroid = sensor_data.mean().values
    distances = np.linalg.norm(sensor_data - centroid, axis=1)
    
    # Calcular la media y desviación estándar de las distancias
    mean_distance = np.mean(distances)
    std_distance = np.std(distances)
    
    # Guardar los resultados
    statistics.append([sensor, mean_distance, std_distance])

# Convertir los resultados en DataFrame
stats_df = pd.DataFrame(statistics, columns=["Sensor", "Mean Distance", "Std Deviation"])

# Guardar los resultados en un CSV
stats_df.to_csv(output_file, index=False)
print(f"Estadísticas guardadas en: {output_file}")
