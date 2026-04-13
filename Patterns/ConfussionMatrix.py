#Librerías y módulos necesarios

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import confusion_matrix

import numpy as np

import matplotlib.pyplot as plt

#Carga del conjunto de datos

iris_conj=load_iris(as_frame=(True))

#Identificación de los conjuntos de entrenamiento y de prueba

X_train,X_test,y_train,y_test=train_test_split(iris_conj["data"],iris_conj["target"],random_state=10)

#Elaboración del modelo

knn=KNeighborsClassifier(n_neighbors=5) 

knn.fit(X_train,y_train)

#Ejemplo de clasificación

dimensiones=[5.5,4,1.8,0.5]

X_a_clasificar=np.array([dimensiones])

prediccion=knn.predict(X_a_clasificar)

print("El número correspondiente a la especie que predice el algoritmo es:",format(prediccion))

print("El nombre de la especie correspondiente a ese número es:",

      format(iris_conj['target_names'][prediccion]))

#Realización de predicciones sobre el conjunto de datos de prueba

prediccion_test= knn.predict(X_test)

print("La exactitud del modelo es: {0:.2f}".format(knn.score(X_test,y_test)))   

#Llamada a la función que calcula la matriz de confusión

mat_conf=confusion_matrix(y_true=y_test,y_pred=prediccion_test)

#Trazado de la matriz de confusión

fig,ax=plt.subplots(figsize=(2.5,2.5))

ax.matshow(mat_conf,cmap=plt.cm.Blues,alpha=0.3)

for i in range(mat_conf.shape[0]):

    for j in range(mat_conf.shape[1]):

        ax.text(x=j,y=i,s=mat_conf[i,j],va='center',ha='center')

        plt.xlabel("Valores predichos")

        plt.ylabel("Valores reales")