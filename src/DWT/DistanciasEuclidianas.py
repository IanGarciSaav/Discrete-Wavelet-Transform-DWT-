import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean
import ast

# Cargar los coeficientes R desde el archivo CSV
file_path = "results/resultados_R.csv"
R_df = pd.read_csv(file_path)

# Convertir las cadenas en listas de números
for col in R_df.columns:
    R_df[col] = R_df[col].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Expandir listas dentro de las celdas en una matriz numérica
R_matrices = R_df.apply(lambda row: np.concatenate(row.values), axis=1).tolist()

# Calcular las distancias euclidianas entre cada par de DWTs y guardarlas en una lista
num_batches = len(R_matrices)
distance_list = []

for i in range(num_batches):
    for j in range(i + 1, num_batches):  # Evitar cálculos redundantes
        distance = euclidean(R_matrices[i], R_matrices[j])
        distance_list.append([f"ED{i+1}{j+1}", distance])

# Guardar la lista de distancias en un archivo CSV
distance_df = pd.DataFrame(distance_list, columns=["Par", "Distancia Euclidiana"])
distance_df.to_csv("results/distancias_euclidianas.csv", index=False)

print("Lista de distancias euclidianas guardada en 'distancias_euclidianas.csv'")
