x=True
y=False
z=True
w=False
print(x and y or z or w)

x=5
#Queremos saber si x se encuentra entre 1 y 10
print(x>1 and x<10)

ciudades=["madrid","barcelona","sevilla","valencia"]
print("madrid" in ciudades)

evaluacion={"matemáticas":8.5,"inglés":6.5,"ciencias":7.5,"economía":5.5}
print("informatica" in evaluacion)

#operadores de entidad
print("identidad")
x=1
y=5
z=5
print(x is y)
print(y is z)

x="prueba"
y=x
print(x is y)

x=(300,150,"color blanco")
y=(300,150,"color blanco")
print(x is y)

edad=18
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad, prigao")