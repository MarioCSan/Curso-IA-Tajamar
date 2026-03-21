#Este es el listado inicial de empresas que han solicitado la subvención
empresas=["El Corte Inglés", "ACCIONA", "Endesa", "Fagor", "HP"]
#No quiero perder el contenido de este listado. Crea una copia y sigo trabajando con ella
empresas_copia=empresas
#Supongamos que el sistema realiza una simulación y me indica que HP no cumple con los requisitos.
#Borro HP en la lista que he copiado.
eliminada="HP"
empresas_copia.remove(eliminada)
#Imprimo el nuevo listado de empresas, ya actualizado
print("Esta es la lista copiada y modificada:",empresas_copia)
#Para estar seguro de que la lista inicial no ha sufrido cambios procedo a imprimirla...
print("Esta es la lista original:",empresas)
#Oh, sorpresa, ¡HP no está!

#continua ejemplo

print("¿Y si usamos copy?")
empresas.append("HP")
empresas_copia=empresas.copy()

empresas_copia.remove(eliminada)
print("Esta es la lista copiada y modificada:",empresas_copia)
#Para estar seguro de que la lista inicial no ha sufrido cambios procedo a imprimirla...
print("Esta es la lista original:",empresas)

#Este es el listado inicial de empresas que han solicitado la subvención

empresas=["El Corte Inglés", "ACCIONA", "Endesa", "Fagor", "HP"]

#Las ordenamos de manera permanente

empresas.sort()

print(empresas)

#Este es el listado inicial de empresas que han solicitado la subvención

empresas=["El Corte Inglés", "ACCIONA", "Endesa", "Fagor", "HP"]

#Las ordenamos de manera temporal y mostramos la lista en pantalla

print("Listado ordenado",sorted(empresas))

#Comprobamos que el listado inicial continúa igual

print("Listado inicial",empresas)