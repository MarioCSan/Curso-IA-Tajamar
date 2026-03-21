ciudades=["madrid","barcelona","sevilla","valencia"]
ciudades[3]="bilbao"
print(ciudades[:])
print(ciudades[:2])

## Para añadir un elemento a la lista, se puede usar el método append
ciudades=["madrid","barcelona","sevilla","valencia"]

ciudades.append("bilbao")

ciudades.append("salamanca")

print(ciudades)

## Para insertar un elemento en una posición concreta, se puede usar el método insert
ciudades=["madrid","barcelona","sevilla","valencia"]

ciudades.insert(1,"bilbao")

print(ciudades)

## para eliminar un elemento de la lista, se puede usar del(), pop() o remove()
## La principal particularidad de del() es que, una vez empleada, ya no resulta posible acceder al valor suprimido.
ciudades=["madrid","barcelona","sevilla","valencia"]

ciudades.insert(1,"bilbao")

del ciudades[1]

## POP() devuelve el elemento eliminado, por lo que se puede almacenar en una variable
ciudades=["madrid","barcelona","sevilla","valencia"]

ciud_pop=ciudades.pop()

print(ciud_pop.title(),"acaba de ser eliminada de la lista")

## REMOVE() elimina la primera aparición del elemento que se le indique, por lo que no es necesario conocer su posición
ciudades=["madrid","barcelona","sevilla","valencia"]

ciudades.remove("sevilla")

print(ciudades)