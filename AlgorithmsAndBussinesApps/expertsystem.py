# Base de hechos
x=0
y=0
# Motor de Inferencia
for i in range(1,15):
    if y==2:
        print("Solución satisfactoria: hay dos litros en el recipiente B")
        break
# Base de Reglas
    # Regla 1
    if x==0 and y==0:
        x=3
        y=0
        print("Hay que llenar el recipiente A con 3 litros: (3,0)")
    # Regla 2
    elif x==0 and y==0:
        x=0
        y=4
        print("Hay que llenar el recipiente A con 4 litros: (0,4)")
    # Regla 3
    elif x==3 and y==0:
        x=0
        y=3
        print("Hay que vaciar el recipiente A, con 3 litros, en B: (0,3)")
    # Regla 4
    elif x==0 and y==4:
        x=3
        y=1
        print("Hay que vaciar el recipiente B, que tiene 1 litro, en A: (3,1)")
    # Regla 5
    elif x==0 and y==3:
        x=3
        y=3
        print("Hay que llenar el recipiente A con 3 litros: (3,3)")
    # Regla 6
    elif x==3 and y==1:
         x=0
         y=1
         print("Hay que vaciar el recipiente A, que tiene 3 litros: (0,1)")
    # Regla 7
    elif x==3 and y==3:
        x=2
        y=4
        print("Hay que vaciar el recipiente A, que tiene 3 litros, en B, hasta llegar al nivel 4: (2,4)")
    # Regla 8
    elif x==0 and y==1:
        x=1
        y=0
        print("Hay que vaciar el recipiente B, que tiene 1 litro, en A: (1,0)")
     # Regla 9
    elif x==2 and y==4:
         x=2
         y=0
         print("Hay que vaciar por completo el recipiente B: (2,0)")
    # Regla 10
    elif x==1 and y==4:
        x=1
        y=4
        print("Hay que llenar el recipiente B hasta llegar al nivel 4: (1,4)")
     # Regla 11
    elif x==2 and y==0:
        x=0
        y=2
        print("Hay que vaciar el recipiente A, que tiene 2 litros, en B: (0,2)")
    # Regla 12
    elif x==0 and y==4:
        x=3
        y=1
        print("Hay que vaciar el recipiente B, que tiene 1 litro, en A: (3,1)")
    # No hay solución
    ## else: print("Solución no encontrada")
    ## solucion
    # No se cumple ninguna de las condiciones anteriores
    #Vaciamos ambos recipientes y actuamos desde el supuesto x=0, y=0
    else:
        x=0
        y=0
        print("Tenemos que vaciar los dos recipientes: (0,0)")