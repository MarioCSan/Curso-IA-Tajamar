import json
A=input("El teléfono suena (True/False): ")

B=input("¿Tienes deseos de responder a la llamada? (True/False): ")

C=input("¿Vas a hacer una llamada? (True/False): ")

A=json.loads(A.lower())

B=json.loads(B.lower())

C=json.loads(C.lower())

print(A, B, C)

if (((not A) and C) or (A and B)):

    D=True

else:

    D=False

if D==True:

    print("El teléfono se descuelga")

else:

    print("El teléfono no se descuelga")