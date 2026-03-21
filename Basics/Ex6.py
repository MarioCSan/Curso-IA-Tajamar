import json

def condicional(elemento1, elemento2):
    return (not elemento1) or elemento2

A = input("calor primera premisa(true/false):")
B = input("valor de la segunda premisa (true/false):")

A= json.loads(A.lower())
B=json.loads(B.lower())

print("el resultado es: ", condicional(A,B))