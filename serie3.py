def contar_letra_en_string(cadena, letra):
    cadena = cadena.lower()
    letra = letra.lower()
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

cadena_ingresada = input("Ingrese una cadena de texto: ")
letra_ingresada = input("Ingrese una letra: ")

cantidad_repeticiones = contar_letra_en_string(cadena_ingresada, letra_ingresada)

print(f"La letra '{letra_ingresada}' se repite {cantidad_repeticiones} veces en la cadena.")
