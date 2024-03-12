def numero_vocales(texto):
    vocales = "aeiouáéíóú"
    contador = 0
    for caracter in texto.lower():
        if caracter in vocales:
            contador += 1
    return contador 

palabra = input("intoduce un animal:")
print("el número de vocales es: ", numero_vocales(palabra))