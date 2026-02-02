#include <ArduinoJson.h>  // Si necesitas cargar o almacenar un archivo JSON

// Parámetros del modelo de Árbol de Decisión (cargados desde el JSON)
const char* classes[] = {"fotorresistencia_data.csv", "sensorSonido_data.csv", "termistor_data.csv"};
const float thresholds[] = {1272.7117004394531, 228.5242213010788, -2.0, -2.0, 610.6724090576172, -2.0, -2.0};
const int features[] = {0, 1, -2, -2, 1, -2, -2};

// Definición de variables para tomar 50 medidas cada 100ms
const int numMeasures = 50;  // Número de medidas que vamos a tomar
float sensorData[numMeasures];  // Array para almacenar las 50 lecturas
int measureIndex = 0;  // Índice para almacenar las lecturas

// Configuración del puerto serie
void setup() {
  Serial.begin(115200);  // Iniciar comunicación serial
  while (!Serial) {}  // Esperar a que se conecte el puerto serial

  Serial.println("Iniciando...");
}

void loop() {
  // Solo tomaremos decisiones cuando tengamos las 50 lecturas necesarias
  unsigned long currentMillis = millis();
  
  // Tomar una medida cada 100ms
  if (currentMillis % 100 == 0 && measureIndex < numMeasures) {
    sensorData[measureIndex] = analogRead(A0);  // Tomar lectura de A0
    measureIndex++;
  }

  // Una vez que tenemos las 50 lecturas, procesamos
  if (measureIndex >= numMeasures) {
    // Imprimir las lecturas obtenidas
    Serial.println("Lecturas obtenidas:");
    for (int i = 0; i < numMeasures; i++) {
      Serial.print(sensorData[i]);
      Serial.print(" ");
    }
    Serial.println();

    // Clasificar el tipo de sensor utilizando los umbrales predefinidos
    String sensorType = classify(sensorData);
    
    // Mostrar el resultado
    Serial.print("Tipo de Sensor Detectado: ");
    Serial.println(sensorType);

    // Reiniciar el índice para nuevas lecturas
    measureIndex = 0;  // Reiniciamos el índice para empezar a tomar nuevas medidas
  }
}

// Función para clasificar el tipo de sensor
String classify(float data[]) {
  // Tomamos el valor unitario (sin cálculos de media o desviación estándar)
  for (int i = 0; i < sizeof(thresholds) / sizeof(thresholds[0]); i++) {
    if (features[i] != -2) {  // Solo consideramos las características definidas, ignoramos las que están en -2
      float threshold = thresholds[i];
      
      // Comparar el valor de la característica con el umbral
      if (features[i] == 0) {  // Comparar 'Mean Distance' (en este caso, valor unitario)
        for (int j = 0; j < numMeasures; j++) {
          if (data[j] > threshold) {
            return classes[i];
          }
        }
      } else if (features[i] == 1) {  // Comparar 'Std Deviation' (en este caso, valor unitario)
        for (int j = 0; j < numMeasures; j++) {
          if (data[j] > threshold) {
            return classes[i];
          }
        }
      }
    }
  }

  return "Sensor desconocido"; // Si no se cumple ninguna condición
}
