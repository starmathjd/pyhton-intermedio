mi_diccionario = {
    "nombre": "David",
    "edad": 39,
    "curso": "Python Intermedio"
}

clave = input("¿Qué clave quieres consultar del diccionario?: ")
print(mi_diccionario)
try:
    valor = mi_diccionario[clave]
except KeyError:
    print(f"Error: La clave '{clave}' no existe en el diccionario.")
else:
    print(f"El valor de '{clave}' es: {valor}")
