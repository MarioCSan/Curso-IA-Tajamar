edad=int(input("Introduce tu edad: "))

if edad<3:
    print("Entrada gratuita")
elif edad>=3 and edad<18:
    print("Entrada reducida de 10 euros")
else:
    print("Entrada normal de 20 euros")        


edad=int(input("Introduce la edad de la persona para la que se va a comprar la entrada: "))
if edad<3:
    precio=0
elif edad<18:
    precio=10      
else:
    precio=20
print("El precio de la entrada para esta persona es de", precio, "€")