import pandas as pd
import json
from sklearn.tree import DecisionTreeClassifier

# Cargar los datos de las firmas y estadísticas
signatures_file = "../../results/sensores/signatures.csv"
statistics_file = "../../results/sensores/statistics.csv"

signatures_df = pd.read_csv(signatures_file)
statistics_df = pd.read_csv(statistics_file)

# Unir ambos archivos en un solo dataframe (asumiendo que tienen una columna común 'Sensor')
data = pd.merge(signatures_df, statistics_df, on="Sensor")

# Seleccionar las columnas necesarias para el entrenamiento
features = data[['Mean Distance', 'Std Deviation']]  # Características
labels = data['Sensor']  # Etiquetas de los sensores

# Entrenar el modelo de Árbol de Decisión
tree = DecisionTreeClassifier(random_state=42)
tree.fit(features, labels)

# Obtener los parámetros del árbol de decisión
# Los parámetros clave son los umbrales, características y las clases
tree_params = {
    "classes": list(tree.classes_),  # Etiquetas de los sensores
    "feature_names": ['Mean Distance', 'Std Deviation'],  # Nombres de las características
    "thresholds": tree.tree_.threshold.tolist(),  # Umbrales de decisión
    "features": tree.tree_.feature.tolist()  # Índices de las características
}

# Guardar los datos del árbol en un archivo JSON
model_file = "../../results/sensores/decision_tree_model.json"
with open(model_file, 'w') as f:
    json.dump(tree_params, f)

print(f"Modelo de Árbol de Decisión guardado en: {model_file}")
