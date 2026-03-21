from datetime import datetime

#Generamos el listado con números pseudoaleatorios

import random

random.seed(25)

lista=[]

for i in range(0,50000):

    num_aleat=random.randint(0,100000)

    lista.append(num_aleat)

#Función de ordenación por selección

def seleccion(lista):

     cont=len(lista)

     for i in range(0,cont-1):

        pos_menor=i

        for j in range(i+1,cont):

            if lista[j]<lista[pos_menor]:

                pos_menor=j

            if pos_menor!=1:

                aux=lista[pos_menor]

                lista[pos_menor]=lista[i]

                lista[i]=aux

     return(lista)

#Llamamos al algoritmo de ordenación que corresponda

t_inic_seleccion=datetime.now()

seleccion(lista)

t_fin_seleccion=datetime.now()

print("Tiempo invertido en la ordenación: ",t_fin_seleccion-t_inic_seleccion)