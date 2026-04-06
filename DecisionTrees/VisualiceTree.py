#Importamos el conjunto de datos y la función requerida para la elaboración del árbol

from sklearn.datasets import load_iris

from sklearn.tree import DecisionTreeClassifier

from sklearn.tree import export_graphviz

from pydotplus import graph_from_dot_data

#Cargamos en X la longitud y anchura del pétalo de cada observación

#En y se vuelca la clasificación de cada lirio (0, 1, 2)

iris=load_iris()

X=iris.data[:,2:]

y=iris.target

#Creamos un objeto arbol_clf con todos los atributos asociados a la construcción 

#del DecisionTreeClassifier

arbol_clf=DecisionTreeClassifier(max_depth=2)

arbol_clf.fit(X,y)

arbol_data=export_graphviz(arbol_clf, out_file=None,feature_names=iris.
                           feature_names[2:],class_names=iris.target_names,rounded=True,filled=True)

grafica=graph_from_dot_data(arbol_data)

grafica.write_png("arbol0.png")