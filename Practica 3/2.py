def buscar_palabra(palabra_buscada, *args):
    resultado = "Palabra encontrada" if palabra_buscada in args else "Palabra no encontrada"
    return resultado

palabras = input("Ingresa una lista de palabras separadas por espacios: ").split()
palabra = input("Ingresa la palabra a buscar: ")

print(buscar_palabra(palabra, *palabras))