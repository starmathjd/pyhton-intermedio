def calcular_promedio(*args):
    promedio = sum(args) / len(args) if args else "No se ingresaron números"
    return promedio

numeros = input("Ingresa una lista de números separados por espacios: ").split()
numeros = [float(num) for num in numeros]  

print(f"El promedio es: {calcular_promedio(*numeros)}")