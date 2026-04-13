import numpy as np
import mglearn
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# -----------------------------
# 1. Cargar datos
# -----------------------------
iris = load_iris()
X = iris.data[:, 2:]   # solo petal length y petal width


# -----------------------------
# 2. KMeans (CAMBIAR AQUÍ: 2, 3 o 4)
# -----------------------------
n_clusters = 4

kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
kmeans.fit(X)


# -----------------------------
# 3. Resultados
# -----------------------------
print("Centroides:\n", kmeans.cluster_centers_)


# -----------------------------
# 4. Visualización clusters
# -----------------------------
mglearn.discrete_scatter(
    X[:, 0], X[:, 1],
    kmeans.labels_,
    markers="o"
)

# Centroides (IMPORTANTE: array dinámico)
mglearn.discrete_scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    list(range(n_clusters)),
    markers="^",
    markeredgewidth=4
)


# -----------------------------
# 5. Nueva predicción
# -----------------------------
X_nuevo = np.array([[2.5, 1]])

print("Clúster asociado:", kmeans.predict(X_nuevo))
print("Distancia a centroides:\n", kmeans.transform(X_nuevo))


# -----------------------------
# 6. Mostrar gráfico
# -----------------------------
plt.title(f"KMeans con {n_clusters} clusters")
plt.show()