
## Escribe un código en Python para mostrar en pantalla la frase «La lluvia en Sevilla es una maravilla» empleando, 
# necesariamente, la lista ciudades, que tienes en la siguiente imagen. 
# Fíjate en que en esta lista “sevilla” aparece en minúsculas.
ciudades =["madrid","barcelona","sevilla","valencia"]
print("la lluvia en " + ciudades[2].title() + " es una maravilla")


## inicializa una lista con los nombres de las siguientes ciudades candidatas a albergar un futuro Mundial de fútbol: Madrid, Nueva York, Pekín, Tokio y Berlín. 
# En la primera criba se ha eliminado a Nueva York de la lista debido a que no cuenta con suficientes infraestructuras. 
# Escribe el código para actualizar la lista y para que salga en pantalla un mensaje informando de la ciudad que ha sido eliminada y el motivo. 
# Piensa en que estás escribiendo el código antes de saber de qué ciudad se tratará (aunque el motivo de la eliminación es el que te he indicado) y
#  que te notificarán de cuál se trata a través de una variable llamada notificacion. 
# Incorpora también el código necesario para incluir una segunda frase, que diga: «Las dos ciudades que encabezan ahora el listado son Madrid y Pekín», 
# de modo que ambas ciudades se obtengan de la lista ya modificada.



candidatas = ["Madrid", "Nueva York", "Pekín", "Tokio", "Berlín"]

candidatas_copia = candidatas.copy()
notificacion = "Nueva York"
candidatas_copia.remove(notificacion)
print(notificacion,"ha sido eliminada porque no cuenta con suficientes infraestructuras")
print("Las dos ciudades que encabezan ahora el listado son",candidatas_copia[0],"y",candidatas_copia[1])