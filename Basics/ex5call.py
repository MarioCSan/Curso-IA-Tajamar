import ex5func as c

import json
A=input("Valor de la primera premisa (True/False):")
B=input("Valor de la primera premisa (True/False):")
A=json.loads(A.lower())
B=json.loads(B.lower())
print("El resultado es:", c.condicional(A,B))