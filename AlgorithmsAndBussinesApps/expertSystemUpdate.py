# Base de Conocimiento: Definimos los límites de los recipientes
CAP_A = 3
CAP_B = 4
META = 2

def resolver_jarras():
    # Estado inicial: (jarra_a, jarra_b)
    estado = (0, 0)
    camino = [estado]
    visitados = {estado}

    print(f"Estado inicial: {estado}")

    while estado[1] != META:
        x, y = estado
        posibles_movimientos = [
            (CAP_A, y, "Llenar A"),
            (x, CAP_B, "Llenar B"),
            (0, y, "Vaciar A"),
            (x, 0, "Vaciar B"),
            (x - min(x, CAP_B - y), y + min(x, CAP_B - y), "Trasvasar A -> B"),
            (x + min(y, CAP_A - x), y - min(y, CAP_A - x), "Trasvasar B -> A")
        ]

        exito_en_paso = False
        for nx, ny, msg in posibles_movimientos:
            nuevo_estado = (nx, ny)
            if nuevo_estado not in visitados:
                print(f"{msg}: ({nx}, {ny})")
                estado = nuevo_estado
                visitados.add(estado)
                camino.append(estado)
                exito_en_paso = True
                break # Elige el primer movimiento válido encontrado

        if not exito_en_paso:
            print("No se encontró solución desde este estado o hay un bucle.")
            return None

    print(f"--- Solución alcanzada: {estado[1]} litros en B ---")
    return camino

resolver_jarras()
