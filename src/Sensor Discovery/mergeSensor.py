import pandas as pd
import os

# Ruta de la carpeta donde están los archivos CSV
folder_path = "../../results/sensores/"
output_file = "../../results/sensores/merged_sensors_data.csv"

# Obtener la lista de archivos CSV en la carpeta
csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

# Lista para almacenar los DataFrames
dataframes = []

# Leer cada archivo CSV y agregarlo a la lista
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    try:
        df = pd.read_csv(file_path)
        df["Sensor"] = file  # Agregar una columna indicando el sensor
        dataframes.append(df)
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")

# Concatenar todos los DataFrames
if dataframes:
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    # Guardar el archivo combinado
    merged_df.to_csv(output_file, index=False)
    print(f"Archivo combinado guardado en: {output_file}")
else:
    print("No se encontraron archivos CSV para combinar.")
