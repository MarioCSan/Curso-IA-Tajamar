#Llamaremos a nuestra función como func_esp. 

#Requiere como argumentos los dos números sobre los que vamos a operar

def func_esp(x,y):

    resultado=(x+y)/(x-y)

#A la conclusión de la operativa de la función devolvemos el número calculado

    return(resultado)


var1=45
var2=36

print(func_esp(var1,var2))