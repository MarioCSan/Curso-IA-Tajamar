ciudades=["madrid","barcelona","sevilla","valencia"]
print("Las ciudades que forman parte de la lista son: \n")
i=0
for ciudad in ciudades:
    print(ciudad)
    i=i+1
print("Hay",i,"ciudades en la lista")

contador=1
while contador<=10:
    print(contador)
    contador+=1

amigos=["pedro","juan","antonio","juan","miguel","fernando","juan"]
#Queremos eliminar todos los "juan" de la lista. Si aplicamos remove() solo se borrar el primero de los "juan"
amigos.remove("juan")
print("Primer borrado:",amigos)
#La salida es Primer borrado: ['pedro', 'antonio', 'juan', 'miguel', 'fernando', 'juan']
#Volvemos a incorporar a "juan" al listado para tener la lista original
amigos.insert(1, "juan")
print("Lista inicial:",amigos)
#La salida es Lista inicial: ['pedro', 'juan', 'antonio', 'juan', 'miguel', 'fernando', 'juan']
#Ahora sí aplicamos el bucle correcto de borrado
while "juan" in amigos:
    amigos.remove("juan")
print("Borrado definitivo:",amigos)
#La salida es Borrado definitivo: ['pedro', 'antonio', 'miguel', 'fernando']
