import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_score

#Generamos el conjunto de datos

centros_blob = np.array([[1.5,2.4],[0.5,2.3],[-0.5,2],[-1,3],[-1.5,2.6]])

blob_std = np.array([0.3, 0.25, 0.1, 0.1, 0.1])

X, y = make_blobs(n_samples=800, centers=centros_blob, cluster_std=blob_std,random_state=20) 

#Creamos las clases KMeans para cada agrupación y las instanciamos

kmeans_por_k = [KMeans(n_clusters=k, random_state=20).fit(X)

                for k in range(1, 11)]

siluetas = [silhouette_score(X, model.labels_)

                     for model in kmeans_por_k[1:]]

#Dibujamos la gráfica

plt.figure(figsize=(8, 3.5))

plt.plot(range(2, 11), siluetas, "bo-")

plt.xlabel("Valores de k", fontsize=14)

plt.ylabel("Índice silueta", fontsize=14)

plt.show()