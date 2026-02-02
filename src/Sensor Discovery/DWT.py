import pandas as pd
import pywt
import numpy as np

# Ruta del archivo combinado
csv_file = "../../results/sensores/merged_sensors_data.csv"
output_file = "../../results/sensores/wavelet_coefficients.csv"

# Cargar los datos
try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Verificar que las columnas necesarias existen
if "Voltage" not in df.columns or "Sensor" not in df.columns:
    print("Error: No se encontraron las columnas necesarias en el archivo CSV.")
    exit()

# Aplicar la Transformada Wavelet Discreta (DWT) con la wavelet Haar
coefficients = []
wavelet = "haar"

# Número de datos por batch y número de batches por sensor
batch_size = 128
batches_per_sensor = 10

# Obtener la lista de sensores únicos
sensors = df["Sensor"].unique()

for sensor in sensors:
    sensor_data = df[df["Sensor"] == sensor]
    
    for i in range(0, batch_size * batches_per_sensor, batch_size):
        batch = sensor_data["Voltage"].iloc[i:i+batch_size]
        if len(batch) < batch_size:
            break  # Evitar procesar lotes incompletos
        
        # Aplicar DWT
        cA, cD = pywt.dwt(batch, wavelet)
        
        # Guardar los coeficientes junto con el nombre del sensor
        coefficients.append([sensor] + list(np.concatenate((cA, cD))))

# Convertir los coeficientes en DataFrame
coeff_columns = ["Sensor"] + [f"Coeff_{i}" for i in range(len(coefficients[0]) - 1)]
coeff_df = pd.DataFrame(coefficients, columns=coeff_columns)

# Guardar el resultado en un CSV
coeff_df.to_csv(output_file, index=False)
print(f"Coeficientes wavelet guardados en: {output_file}")
