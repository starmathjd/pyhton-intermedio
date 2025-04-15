def verificar_argumentos(*args):
    # Verificamos si hay al menos 2 argumentos
    if len(args) < 2:
        return "Error: No se han pasado suficientes argumentos."
    else:
        return "Argumentos suficientes."


print(verificar_argumentos(1, 2))  # Prueba con suficientes argumentos
print(verificar_argumentos(1))     # Prueba con insuficientes argumentos
