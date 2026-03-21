#Un ejemplo de tupla
especificaciones=(300,150,"color blanco")
#El elemento de la posición 0 es 300. Para mostrarlo empleamos los corchetes, de manera similara a las listas
print(especificaciones[0])
#Si tratamos de hacer algún cambio el sistema devuelve un error
#especificaciones[2]="color amarillo" -> esto falla
especificaciones=(300,150,"color amarillo")



## conjuntos
conj_1={2,4,6,8}
print(conj_1)

conj_2={2,4,4,6,8,8}

print(conj_2)

# conj_3={[2,4],[6,8]}

# print(conj_3)

conj_3=set([2,4,6,8])

print(conj_3)

##Diccionario 
evaluacion={"matemáticas":8.5,"inglés":6.5,"ciencias":7.5,"economía":5.5}
print(evaluacion)
print("La nota en matemáticas es:",evaluacion["matemáticas"])

evaluacion={}
evaluacion["matemáticas"]=8.5
evaluacion["inglés"]=6.5
evaluacion["ciencias"]=7.5
evaluacion["economía"]=5.5
print(evaluacion)
print("La nota en matemáticas es:",evaluacion["matemáticas"])


#Para eliminar un elemento del diccionario se puede usar del() o pop()
del(evaluacion["ciencias"])

print(evaluacion)

## get() devuelve el valor asociado a la clave que se le indique, pero si la clave no existe no devuelve un error, sino un mensaje que se le puede personalizar
valor_mates=evaluacion.get("matemáticas")

print(valor_mates)

## segundo argumento de get() es el mensaje que se devuelve si la clave no existe
evaluacion={}

evaluacion["matemáticas"]=8.5

evaluacion["inglés"]=6.5

evaluacion["ciencias"]=7.5

evaluacion["economía"]=6.0

valor_informatica=evaluacion.get("informática","No existe nota de informática")

valor_ingles=evaluacion.get("inglés","No existe nota de inglés")

print("Nota de informática:",valor_informatica)

print("Nota de inglés:",valor_ingles)