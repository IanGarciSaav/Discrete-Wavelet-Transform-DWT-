# Discrete-Wavelet-Transform-DWT-
This was a project I completed for my industrial cybersecurity course, using mathematical formulations to send a large amount of data through an ESP8266.

# DWT Sensor Identification Project

This project implements a sensor identification system using Discrete Wavelet Transform (DWT) for feature extraction and Euclidean distance/Machine Learning for classification. It is designed to analyze signals from sensors (e.g., connected via ESP8266) and identify them based on their unique "fingerprint" or signal characteristics.

## Project Structure

The project is organized as follows:

- **`src/DWT`**: Contains the core signal processing logic.
    - `main.py`: Main entry point for the offline analysis pipeline.
    - `DWT.py`: Performs the Haar Discrete Wavelet Transform on dataset data.
    - `DistanciasEuclidianas.py`: Calculates Euclidean distances between DWT coefficients.
    - `Media&DeviacionEstandar.py`: Calculates statistics (Mean, Std Dev) from the distances.
- **`src/Sensor Discovery`**: Contains scripts for real-time data collection and machine learning models.
    - `mediciones_sensores.py`: Captures real-time voltage data from an ESP8266 via serial port.
    - `model.py`: Trains a Decision Tree classifier to identify sensors based on signal statistics.
- **`data`**: Stores input datasets (e.g., `dataset320.csv`).
- **`results`**: Stores output files, including processed coefficients, distance matrices, and the trained model.

## Dependencies

This project requires **Python 3.x** and the following libraries:

```bash
pip install numpy pandas matplotlib scipy scikit-learn pyserial
```

## Inputs and Outputs

### Inputs
1.  **`data/dataset320.csv`**: A CSV file containing raw sensor signal data for offline analysis.
2.  **Serial Data**: Real-time voltage readings from a sensor connected via an ESP8266 microcontroller (baud rate 115200).

### Outputs
1.  **`results/resultados_R.csv`**: Contains the extracted DWT coefficients (Feature Vector R).
2.  **`results/distancias_euclidianas.csv`**: A matrix or list of Euclidean distances between signal features.
3.  **`results/sensores/decision_tree_model.json`**: The trained Decision Tree model parameters (thresholds, features, classes).
4.  **Plots**: The `DWT.py` script generates plots visualizing the Approximation and Detail coefficients of the signal.

## How to Run

### 1. Offline Analysis Pipeline
To run the full analysis on the stored dataset (`dataset320.csv`), execute the main script from the `src/DWT` directory:

```bash
python src/DWT/main.py
```
*Note: This script automatically triggers `DWT.py`, `DistanciasEuclidianas.py`, and `Media&DeviacionEstandar.py` in sequence.*

### 2. Real-time Data Collection
To collect new data from a sensor connected to an ESP8266:
1.  Connect the ESP8266 to your computer.
2.  Update the `serial_port` variable in `src/Sensor Discovery/mediciones_sensores.py` to match your COM port (e.g., `COM5`).
3.  Run the script:
    ```bash
    python "src/Sensor Discovery/mediciones_sensores.py"
    ```
    This will save 1280 data points to `results/sensorProximidad_data.csv`.

### 3. Training the Identification Model
To train the Decision Tree model using processed statistics:
1.  Ensure you have `results/sensores/signatures.csv` and `results/sensores/statistics.csv` (generated from your data collection and processing steps).
2.  Run the model training script:
    ```bash
    python "src/Sensor Discovery/model.py"
    ```
    The trained model parameters will be saved to `results/sensores/decision_tree_model.json`.

## Methodology (Inferred from DWT.pdf context)
1.  **Data Acquisition**: Raw signals are captured from sensors.
2.  **Preprocessing**: Signals are segmented into batches (e.g., size 16 or 32).
3.  **Feature Extraction (DWT)**: 
    - The **Haar Wavelet Transform** decomposes the signal into **Approximation (A)** and **Detail (D)** coefficients.
    - A feature vector **R** is constructed using these coefficients to represent the signal's energy distribution.
4.  **Similarity Measurement**: Euclidean distance is used to compare the feature vector **R** of a new signal against known signatures.
5.  **Classification**: A Decision Tree classifier uses statistical properties (Mean, Std Dev) of these distances to determine the sensor identity.
