Ejercicios Modulo 5. Ficheros (Enunciado)

Ejercicio nº1:
 #Definir el nombre del fichero
nombre_fichero = "pruebas.txt"

try:
    # Abrir el fichero en modo lectura con la codificación UTF-8
    with open(nombre_fichero, "r", encoding="utf8") as archivo:
        # Obtener el estado de cierre del fichero
        esta_cerrado = archivo.closed

        # Obtener el modo de apertura del fichero
        modo_apertura = archivo.mode

        # Mostrar la información
        print("Nombre del fichero:", nombre_fichero)
        print("¿Fichero cerrado?", esta_cerrado)
        print("Modo de apertura:", modo_apertura)

        # Leer y mostrar el contenido del fichero línea por línea
        print("\nContenido del fichero:")
        contenido = archivo.read()
        print(contenido)

except FileNotFoundError:
    print("El fichero no se encuentra.")
except Exception as e:
    print("Ocurrió un error:", e)



Ejercicio nº2:

# Definir el nombre del fichero
nombre_fichero = "pruebas.txt"

try:
    # Abrir el fichero en modo lectura con la codificación UTF-8
    with open(nombre_fichero, "r", encoding="utf8") as archivo:
        # Leer una línea del fichero
        primera_linea = archivo.readline()

        # Mostrar la primera línea
        print("Primera línea del fichero:")
        print(primera_linea)

        # Volver al principio del fichero
        archivo.seek(0)

        # Leer el fichero línea a línea
        print("\nContenido del fichero línea a línea:")
        for linea in archivo:
            print(linea, end="")  # El parámetro end="" evita la inserción de líneas adicionales


Ejercicio nº3:

# Definir el nombre del fichero
nombre_fichero = "pruebas.txt"

try:
    # Abrir el fichero en modo escritura (concatenando) con la codificación UTF-8
    with open(nombre_fichero, "a", encoding="utf8") as archivo:
        # Agregar una nueva línea de texto
        nueva_linea = "Esta es una línea agregada en modo escritura.\n"
        archivo.write(nueva_linea)

    # Comprobar el fichero después de agregar la línea
    with open(nombre_fichero, "r", encoding="utf8") as archivo:
        contenido = archivo.read()
        print("Contenido actual del fichero:")
        print(contenido)

except FileNotFoundError:
    print("El fichero no se encuentra.")
except Exception as e:
    print("Ocurrió un error:", e)


Ejercicio nº4:

# Definir el nombre del fichero
nombre_fichero = "pruebas.txt"

try:
    # Abrir el fichero en modo escritura (sobrescribiendo) con la codificación UTF-8
    with open(nombre_fichero, "w", encoding="utf8") as archivo:
        # Escribir una nueva línea de texto
        nueva_linea = "Este es un nuevo contenido sobrescribiendo el fichero.\n"
        archivo.write(nueva_linea)

    # Comprobar el fichero después de sobrescribir y agregar la línea
    with open(nombre_fichero, "r", encoding="utf8") as archivo:
        contenido = archivo.read()
        print("Contenido actual del fichero:")
        print(contenido)

except FileNotFoundError:
    print("El fichero no se encuentra.")
except Exception as e:
    print("Ocurrió un error:", e)


Ejercicio nº5:

nombre_fichero = "personas.txt"
personas = []

try:
    with open(nombre_fichero, "r", encoding="utf8") as archivo:
        for linea in archivo:
            # Eliminar el salto de línea y dividir la línea en campos utilizando el punto y coma como separador
            campos = linea.strip().split(";")
            id_persona, nombre, apellido, nacimiento = campos

            # Crear un diccionario con los campos
            persona = {
                "id": id_persona,
                "nombre": nombre,
                "apellido": apellido,
                "nacimiento": nacimiento
            }

            # Agregar el diccionario a la lista de personas
            personas.append(persona)

    # Recorrer la lista de personas y mostrar la información de manera amigable
    for persona in personas:
        mensaje = "(id={}) {} {} => {}".format(
            persona["id"], persona["nombre"], persona["apellido"], persona["nacimiento"])
        print(mensaje)

except FileNotFoundError:
    print("El fichero no se encuentra.")
except Exception as e:
    print("Ocurrió un error:", e)





