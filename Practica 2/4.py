archivo_nombre = "archivo_inexistente.txt"

try:
    with open(archivo_nombre, 'r') as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print(f"Archivo no encontrado. Creando el archivo: {archivo_nombre}")
    with open(archivo_nombre, 'w') as archivo:
        archivo.write("Archivo creado porque no existía.")
else:
    print("Archivo leído exitosamente.")