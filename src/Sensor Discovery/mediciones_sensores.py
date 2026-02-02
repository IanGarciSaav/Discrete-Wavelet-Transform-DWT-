import serial
import csv
import time

# Configuración del puerto serial (asegúrate de que el puerto sea el correcto)
serial_port = 'COM5'  # Cambia esto a tu puerto serial
baud_rate = 115200  # Debe coincidir con la configuración del ESP8266
timeout = 0.1  # Tiempo de espera para leer del puerto serial (en segundos)

# Establecer el puerto serial
ser = serial.Serial(serial_port, baud_rate, timeout=timeout)

# Abre el archivo CSV para guardar los datos
csv_filename = '../../results/sensorProximidad_data.csv'

# Contador para los datos
data_count = 0
max_data = 1280  # Limitar a 1280 datos

# Abre el archivo CSV en modo escritura
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Index', 'Voltage'])  # Escribir encabezados

    print("Comenzando a leer datos del puerto serial...")

    while data_count < max_data:
        if ser.in_waiting > 0:  # Si hay datos disponibles para leer
            data = ser.readline()  # Leer la línea del puerto serial como bytes
            try:
                # Si el dato leído es numérico, lo guardamos
                voltage = float(data.decode('ascii').strip())  # Intentar decodificar como texto en ASCII
                data_count += 1
                writer.writerow([data_count, voltage])
                print(f"Guardando dato {data_count}/{max_data}: {voltage}")
            except ValueError:
                # Si no es un número, ignorarlo
                continue

print("Proceso terminado. Datos guardados en el csv.")
ser.close()
