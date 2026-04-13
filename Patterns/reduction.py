import matplotlib.pyplot as plt
import numpy as np

# Creamos la figura, dándole un tamaño adecuado

fig = plt.figure(figsize=(6, 3.8))

# Dibujamos las tres dimensiones

ax1 = fig.add_subplot(111,projection='3d')

# Nube de puntos
x = [1,2,3,4,5,6,7,8,9,10]

y = [2,4,6,8,10,12,14,16,18,20]

z = [3,6,9,12,15,18,21,24,27,30]

# Dibujamos el gráfico de dispersión de estos puntos con la función scatter

ax1.scatter(x, y, z, c='b', marker='o')

# Generar conjunto X
np.random.seed(4)

m = 60

w1, w2 = 0.1, 0.3

noise = 0.1

angles = np.random.rand(m) * 3 * np.pi / 2 - 0.5

X = np.empty((m, 3))

X[:, 0] = np.cos(angles) + np.sin(angles)/2 + noise * np.random.randn(m) / 2

X[:, 1] = np.sin(angles) * 0.7 + noise * np.random.randn(m) / 2

X[:, 2] = X[:, 0] * w1 + X[:, 1] * w2 + noise * np.random.randn(m)

ax1.scatter(X[:, 0], X[:, 1], X[:, 2] , c='b', marker='o')

# Mostramos el gráfico

plt.show()