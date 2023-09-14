Ejercicios Modulo 4. Unidad 2. Métodos aplicados (Soluciones)

Ejercicio nº1:

def verificar_texto(texto):
    if texto.isalpha():
        return "El texto es una cadena de texto"
    elif texto.isdigit():
        return "El texto es una cadena de dígitos"
    elif any(c.isdigit() for c in texto) and any(c.isalpha() for c in texto):
        return "El texto incluye caracteres y números"
    else:
        return "El texto no cumple con ninguna condición especificada"

texto_usuario = input("Por favor, introduce un texto: ")
resultado = verificar_texto(texto_usuario)
print(resultado)

print(type(resultado))

Ejercicio nº2:

def buscar_y_extraer(texto, palabra):
    posicion = texto.find(palabra)
    if posicion != -1:
        resultado = texto[posicion:]
        return resultado
    else:
        return "La palabra no se encontró en el texto"

texto_usuario = input("Introduce un texto: ")
palabra_buscar = input("Introduce la palabra a buscar: ")

resultado = buscar_y_extraer(texto_usuario, palabra_buscar)
print("Resultado:", resultado)
print(type(resultado))

 Ejercicio nº3:

def contar_palabra(lista, palabra):
    contador = 0
    for elemento in lista:
        if elemento == palabra:
            contador += 1
    return contador

frase = input("Introduce una frase: ")
palabra_buscada = "mundo"  # La palabra que deseas buscar

# Dividir la frase en palabras usando el espacio como separador
lista_palabras = frase.split()

print("Lista de palabras:", lista_palabras)
cantidad_mundo = contar_palabra(lista_palabras, palabra_buscada)

print(f"La palabra '{palabra_buscada}' se encuentra {cantidad_mundo} veces en la lista.")

print(type(resultado))
