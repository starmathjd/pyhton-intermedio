try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print(f"Resultado de la división: {resultado}")