# Metodos-de-aprendizaje-no-supervisado
Ejemplo de método de aprendizaje no supervisado
🚌 Clustering de Rutas de TransMilenio - Aprendizaje No Supervisado
Este proyecto consiste en aplicar un modelo de aprendizaje automático no supervisado para agrupar rutas del sistema de transporte masivo TransMilenio en Bogotá, Colombia.

El objetivo es identificar agrupaciones (clusters) entre estaciones de origen y destino para entender mejor cómo se podrían categorizar ciertos trayectos según su ubicación o patrones de conexión.

📁 Contenido del repositorio
datos_transmilenio.xlsx: Base de datos creada manualmente con estaciones de origen, destino y coordenadas.

clustering_transmilenio.py: Script en Python que realiza el clustering usando KMeans.

image.png: Gráfico generado que muestra el resultado del clustering.

README.md: Documento con la descripción del proyecto.

📊 Fuente de datos
No se utilizó una fuente de datos externa. Se construyó un dataset personalizado que simula rutas de TransMilenio. Contiene:

Estación de origen

Estación de destino

Coordenadas geográficas (latitud y longitud)

Este dataset fue creado para fines académicos.

🧠 Modelo de Aprendizaje Automático
Se utilizó el algoritmo KMeans del paquete sklearn para identificar patrones de agrupamiento entre estaciones.

Pasos:
Codificación de estaciones con LabelEncoder.

Agrupamiento de rutas origen-destino.

Visualización de los clusters en un gráfico 2D.

🖼️ Resultados
Se obtuvieron 3 clusters que agrupan trayectos similares. Esto permite visualizar patrones o rutas que podrían optimizarse o estudiarse según cercanía o distribución espacial.

El gráfico generado muestra:

Eje X: estación origen (codificada)

Eje Y: estación destino (codificada)

Color: cluster al que pertenece cada ruta


