import pandas as pd
import matplotlib.pyplot as plt

# Lista de archivos CSV y nombres de sensores
sensor_files = {
    "Fotorresistencia": "../../results/sensores/fotorresistencia_data.csv",
    "Proximidad": "../../results/sensores/sensorProximidad_data.csv",
    "Sonido": "../../results/sensores/sensorSonido_data.csv",
    "Termistor": "../../results/sensores/termistor_data.csv"
}

# Configurar la figura
plt.figure(figsize=(10, 6))

# Leer y graficar cada archivo CSV
for sensor, file in sensor_files.items():
    try:
        df = pd.read_csv(file)
        plt.plot(df['Index'], df['Voltage'], label=sensor)
    except Exception as e:
        print(f"Error al leer {file}: {e}")

# Configurar etiquetas y leyenda
plt.xlabel("Índice de medición")
plt.ylabel("Valor del sensor")
plt.title("Gráfica de los sensores")
plt.legend()
plt.grid()

# Mostrar la gráfica
plt.show()
