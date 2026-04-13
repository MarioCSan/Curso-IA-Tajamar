import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# 1. Carga y preparación de datos
iris = sns.load_dataset("iris")
# Seleccionamos solo longitud y anchura del pétalo (columnas 2 y 3)
X = iris.iloc[:, [2, 3]].values 

# Punto de prueba solicitado
X_new = np.array([[2.5, 1]])

# --- Funciones de apoyo (basadas en tu código previo) ---

def plot_data(X):
    plt.plot(X[:, 0], X[:, 1], 'k.', markersize=4)

def plot_centroids(centroids):
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='o', s=30, linewidths=8, color='w', zorder=10, alpha=0.9)
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=50, linewidths=2, color='k', zorder=11)

def plot_decision_boundaries(clusterer, X, title):
    mins = X.min(axis=0) - 0.5
    maxs = X.max(axis=0) + 0.5
    xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], 1000),
                         np.linspace(mins[1], maxs[1], 1000))
    Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]), cmap="Pastel2")
    plt.contour(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]), linewidths=1, colors='k')
    plot_data(X)
    plot_centroids(clusterer.cluster_centers_)
    
    # Dibujar el punto de prueba (2.5, 1) en rojo para identificarlo
    plt.scatter(X_new[:, 0], X_new[:, 1], color='red', marker='s', s=100, label="Punto (2.5, 1)", zorder=15)
    
    plt.title(title)
    plt.xlabel("Petal Length")
    plt.ylabel("Petal Width")

# --- 2. Ejecución y Comparación de K = 2, 3, 4 ---

k_values = [2, 3, 4]
plt.figure(figsize=(18, 5))

for i, k in enumerate(k_values):
    # Entrenamiento
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(X)
    
    # Cálculos para el punto (2.5, 1)
    cluster_asignado = kmeans.predict(X_new)[0]
    # transform() devuelve la distancia de los puntos a cada centroide
    distancias = kmeans.transform(X_new)[0]
    
    # Visualización
    plt.subplot(1, 3, i + 1)
    plot_decision_boundaries(kmeans, X, f"K-Means con K={k}")
    
    # Impresión de resultados por consola
    print(f"--- Resultados para K={k} ---")
    print(f"Centroides:\n{kmeans.cluster_centers_}")
    print(f"Punto {X_new[0]} asignado al clúster: {cluster_asignado}")
    print(f"Distancias a los centroides: {distancias}\n")

plt.tight_layout()
plt.show()