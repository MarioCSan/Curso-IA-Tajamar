from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import mglearn
import matplotlib.pyplot as plt

# Generamos datos
X, y = make_blobs(random_state=20)

# Modelo KMeans
kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(X)

print("Los clústeres:", kmeans.labels_)
print("Centroides:", kmeans.cluster_centers_)

# Scatter de puntos
mglearn.discrete_scatter(X[:, 0], X[:, 1],
                         kmeans.labels_, markers="o")

# Centroides
mglearn.discrete_scatter(kmeans.cluster_centers_[:, 0],
                         kmeans.cluster_centers_[:, 1],
                         [0, 1, 2],
                         markers="^",
                         markeredgewidth=4)
plt.annotate('Clúster 0',

              xy=(-8.96034004, 3.79161145),

              xytext=(0.025,0.05),

              textcoords='figure fraction',

              fontsize=12,

    arrowprops=dict(facecolor='black', shrink=0.1))

plt.show()