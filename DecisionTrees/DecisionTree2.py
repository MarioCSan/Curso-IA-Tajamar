#Importamos el conjunto de datos, la función requerida para la elaboración del árbol,
#y el método para seleccionar el conjunto de entrenamiento
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from pydotplus import graph_from_dot_data
#Cargamos en X la longitud y anchura del pétalo, tal y como hemos hecho en secciones anteriores. 
#En y se vuelca la clasificación de cada lirio (0, 1, 2)
iris=load_iris()
X=iris.data[:,2:]
y=iris.target
#Extraemos el conjunto de entrenamiento
#El término random_state permite que podamos obtener las veces que deseemos los mismos subconjuntos
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=20)
arbol_clf=DecisionTreeClassifier()
arbol_clf.fit(X_train,y_train)
arbol_data=export_graphviz(arbol_clf,out_file=None,feature_names=iris.feature_names[2:], 
                class_names=iris.target_names,rounded=True,filled=True)
grafica=graph_from_dot_data(arbol_data)
#Generamos la gráfica en formato png, en este caso cambiando la denominación del archivo
grafica.write_png("arbol_nuevo.png")