import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Función para verificar si un número es potencia de 2
def es_potencia_de_dos(n):
    return (n & (n - 1) == 0) and n > 0

# Función que realiza la Transformada Discreta de Haar
def haar_dwt(signal):
    n = len(signal)
    coefficients = []
    while n > 1:
        a = [(signal[i] + signal[i + 1]) / (2 ** 0.5) for i in range(0, n, 2)]
        d = [(signal[i] - signal[i + 1]) / (2 ** 0.5) for i in range(0, n, 2)]
        coefficients.append((a, d))
        signal = a
        n = len(signal)
    return coefficients

# Cargar los datos desde el archivo CSV
file_path = "data/dataset320.csv"
df = pd.read_csv(file_path)

# Extraer la columna de datos (suponiendo que es la primera columna)
data = df.iloc[:, 0].values

# Definir tamaño del lote
batch_size = 16  # 2^5

# Lista para almacenar las Rs
Rs = []

# Procesar en lotes de 32
num_batches = len(data) // batch_size

for batch_idx in range(num_batches):
    batch = data[batch_idx * batch_size:(batch_idx + 1) * batch_size]

    print(f"\nProcesando lote {batch_idx + 1}:")
    print(batch)

    # Aplicar la Transformada de Haar
    dwt_result = haar_dwt(batch.tolist())

    # Imprimir los resultados
    for level, (approx, detail) in enumerate(dwt_result):
        print(f"Nivel {level+1}:")
        print(f" Coeficientes de aproximación: {approx}")
        print(f" Coeficientes de detalle: {detail}")

    # Extraer coeficientes para graficar
    approx_levels = [level[0] for level in dwt_result]
    detail_levels = [level[1] for level in dwt_result]

    # Construir R = [cA_N, cD_N, ..., cD_1]
    R = [approx_levels[-1]] + detail_levels[::-1]
    print("\nR =", R)

    # Guardar R en la lista
    Rs.append(R)

    # Crear figura con subgráficos
    fig, axes = plt.subplots(len(dwt_result) + 1, 2, figsize=(12, 8))

    # Graficar los coeficientes de Haar
    for i, (approx, detail) in enumerate(zip(approx_levels, detail_levels)):
        axes[i, 0].plot(approx, marker='o', linestyle='--', label=f'Approx Nivel {i+1}')
        axes[i, 0].legend()
        axes[i, 0].set_title(f'Coeficientes de Aproximación (Nivel {i+1})')

        axes[i, 1].plot(detail, marker='o', linestyle='--', label=f'Detail Nivel {i+1}', color='r')
        axes[i, 1].legend()
        axes[i, 1].set_title(f'Coeficientes de Detalle (Nivel {i+1}')

    # Graficar R en la última fila
    for i, coef in enumerate(R):
        axes[-1, 0].plot(coef, marker='o', linestyle='--', label=f'R[{i}]')

    axes[-1, 0].legend()
    axes[-1, 0].set_title("Coeficientes de R")

    # Ocultar la última celda derecha para mejor visualización
    axes[-1, 1].axis("off")

    #plt.tight_layout()
    #plt.show()

# Guardar las Rs en un archivo CSV
R_df = pd.DataFrame(Rs)
R_df.to_csv("results/resultados_R.csv", index=False)
