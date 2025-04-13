import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from geopy.distance import geodesic

# Ejemplo de estaciones de TransMilenio (origen, destino y sus coordenadas)
data = {
    "Origen": ["Alquería", "Portal Norte", "Calle 26", "Ricaurte", "Tunal", "Flores", "Calle 100", "Portal Sur", "Av. Jiménez", "Alquería"],
    "Destino": ["Tinis - Gato Dumas", "Universidades", "Portal Norte", "Calle 72", "Banderas", "Calle 100", "Calle 26", "Flores", "Portal 80", "Bosa"],
    "Coordenadas_Origen": [(4.5563, -74.1232), (4.5639, -74.0756), (4.6001, -74.0725), (4.6152, -74.0721), (4.5581, -74.1187), (4.6034, -74.0831), (4.6199, -74.0732), (4.6031, -74.0932), (4.6094, -74.1015), (4.5563, -74.1232)],
    "Coordenadas_Destino": [(4.5632, -74.1181), (4.5981, -74.0675), (4.5639, -74.0756), (4.5772, -74.0772), (4.6020, -74.1201), (4.6332, -74.0605), (4.5900, -74.0700), (4.6232, -74.1040), (4.5756, -74.1194), (4.5985, -74.1567)]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Calcular distancias entre origen y destino usando geopy
def calcular_distancia(coord1, coord2):
    return geodesic(coord1, coord2).km

# Aplicar función de distancia al DataFrame
df["Distancia"] = [calcular_distancia(row["Coordenadas_Origen"], row["Coordenadas_Destino"]) for _, row in df.iterrows()]

# Codificar las estaciones de origen y destino con LabelEncoder
le_origen = LabelEncoder()
le_destino = LabelEncoder()

df["Origen_encoded"] = le_origen.fit_transform(df["Origen"])
df["Destino_encoded"] = le_destino.fit_transform(df["Destino"])

# Seleccionar las características para el clustering (en este caso las coordenadas codificadas y distancia)
X = df[["Origen_encoded", "Destino_encoded", "Distancia"]]

# Aplicar K-Means para agrupar las rutas en 3 clusters (puedes cambiar el número de clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Ver los resultados
print(df[["Origen", "Destino", "Distancia", "Cluster"]])

# Visualización de los clusters
plt.scatter(df["Origen_encoded"], df["Destino_encoded"], c=df["Cluster"], cmap='viridis')
plt.xlabel("Estación Origen (Codificada)")
plt.ylabel("Estación Destino (Codificada)")
plt.title("Clustering de Rutas de TransMilenio")
plt.colorbar(label='Cluster')
plt.show()

