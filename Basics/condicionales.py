print("Introduce tu edad:")

edad=int(input())

if edad>=18:

    print("Eres mayor de edad")

    print("¿Quieres sacarte el carnet de conducir?")

else:
    print("Lo sentimos, todavía no tienes edad para sacarte el carnet de conducir")

    print("Introduce tu edad:")

edad=float(input())

if edad>=18:

    print("Eres mayor de edad")

    print("¿Quieres sacarte el carnet de conducir?")

else:

    print("Lo sentimos, todavía no tienes edad para sacarte el carnet de conducir")

    edad=int(input("Introduce tu edad: "))

if edad>=18:

    print("Eres mayor de edad")

    print("¿Quieres sacarte el carné de conducir?")

else:
    print("Lo sentimos, todavía no tienes edad para sacarte el carnet de conducir")

    edad=int(input("Introduce tu edad: "))

carn_cond=input("¿Posees el carné de conducir B? (Sí / No): ")

if edad<18:

       print("Lo sentimos, todavía no tienes edad para sacarte el carné de conducir")

elif carn_cond == "No":

    print("¿Quieres sacarte el carné de conducir?")

else:

    print("¿Quieres sacarte otro carné, diferente al B?")

edad=int(input("Introduce tu edad: "))
carn_cond=input("¿Posees el carné de conducir B? (Sí / No): ")
if edad<18:
    print("Lo sentimos, todavía no tienes edad para sacarte el carné de conducir")
elif carn_cond == "No":
    sacar_carn=input("¿Quieres sacarte el carné de conducir? (Sí / No): ")
    if sacar_carn =="Sí":
        print("Excelente idea. Nuestra autoescuela te ofrece un precio imbatible")
    else:
        print("¿Por qué no te lo piensas? Nos encontramos en un momento ideal para sacar el carné")
else:
        nuevo_carn=input("¿Quieres sacarte otro carné, diferente al B?")
        if nuevo_carn=="Sí":
            print("Marque en la pantalla qué carné quieres conseguir")
        else:
            print("Gracias por acceder a nuestra página web")