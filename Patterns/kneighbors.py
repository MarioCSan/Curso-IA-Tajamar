#Librerías y módulos necesarios

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

import numpy as np   

import matplotlib.pyplot as plt

#Carga del conjunto de datos

iris_conj=load_iris(as_frame=(True))

#Identificación de los conjuntos de entrenamiento y de prueba

X_train,X_test,y_train,y_test=train_test_split(iris_conj["data"],iris_conj["target"],random_state=0)

#Elaboración del modelo

knn=KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)

#Ejemplo de clasificación de una nueva flor

dimensiones=[5.5,4,1.8,0.5]

X_a_clasificar=np.array([dimensiones])

prediccion=knn.predict(X_a_clasificar)

prediccion_test= knn.predict(X_test)

print("Predicciones realizadas:\n",prediccion_test)

print("El número correspondiente a la especie que predice el algoritmo es:",format(prediccion))

print("El nombre de la especie correspondiente a ese número es:",format(iris_conj['target_names'][prediccion]))

print("La exactitud del modelo es:", np.mean((prediccion_test==y_test)))

print("La exactitud del modelo es: {0:.2f}".format(knn.score(X_test,y_test)))

from sklearn.metrics import confusion_matrix

mat_conf=confusion_matrix(y_true=y_test,y_pred=prediccion_test)

print("La matriz de confusión es:",mat_conf)

fig,ax=plt.subplots(figsize=(2.5,2.5))
ax.matshow(mat_conf,cmap=plt.cm.Blues,alpha=0.3)

for i in range(mat_conf.shape[0]):

    for j in range(mat_conf.shape[1]):

        ax.text(x=j,y=i,s=mat_conf[i,j],va='center',ha='center')

plt.xlabel("Valores predichos")
plt.ylabel("Valores reales")

plt.show()