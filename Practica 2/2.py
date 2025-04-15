try:
    num = float(input("Introduce un número: "))
    cadena = str(input("Introduce un string: "))
    resultado = num + cadena
except TypeError:
    print("Error: No se puede sumar un número con un string.")
else:
    print(f"Resultado de la suma: {resultado}")