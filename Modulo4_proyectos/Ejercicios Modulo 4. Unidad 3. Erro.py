 Ejercicios Modulo 4. Unidad 3. Errores y Excepciones

1) Código a evaluar:
try:
    numero = 7 / 0
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")

''''''Al usar este bloque de manejo de excepciones, si ocurre la excepción ZeroDivisionError, 
      se imprimirá el mensaje,"Error: No es posible dividir entre cero."
    en lugar de mostrar el traceback completo y detener la ejecución del programa''''''


2) Código a evaluar:
lista = [4, 7, 30, 23, 5]

try:
    elemento = lista[10]
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")
    
'''''' Al usar este bloque de manejo de excepciones, si ocurre la excepción IndexError,  
       se imprimirá el mensaje "Error: El índice está fuera del rango de la lista."
      en lugar de mostrar el traceback completo y detener la ejecución del programa''''''


3) Código a evaluar:
paises = { "españa": "español", "eeuu": "inglés", "italia": "italiano" }

try:
    idioma = paises["alemania"]
except KeyError:
    print("Error: El país no se encuentra en la lista de países.")
    
''''''Al usar este bloque de manejo de excepciones, si ocurre la excepción KeyError, 
      se imprimirá el mensaje "Error: El país no se encuentra en la lista de países." 
      en lugar de mostrar el traceback completo y detener la ejecución del programa.'''''' 

4) Localiza el error en el siguiente bloque de código.  Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
try:
    resultado = "2" + 10
except TypeError:
    print("Error: No se pueden concatenar una cadena y un número.")
    
''''''Al usar este bloque de manejo de excepciones, si ocurre la excepción TypeError, 
      se imprimirá el mensaje "Error: No se pueden concatenar una cadena y un número." 
       en lugar de mostrar el traceback completo y detener la ejecución del programa.''''''
    
resultado = "2" + str(10)

''''''La solución para este caso sería convertir el número entero en una cadena  antes 
     de la concatenación, usando la función str():De esta manera, el número 10 se convertirá
    en la cadena "10" y luego se podrá concatenar correctamente con la cadena "2".''''''  

5) Realiza una función llamada agregar_sin_repetidos() que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

```
  Error: Imposible añadir elementos duplicados => [elemento].
```
Prueba a agregar los elementos 7, "Python" y 5 a través de la función agregar_sin_repetidos() e imprime la lista completa al finalizar.

Pista: Puedes utilizar la sintaxis: elemento in lista

def agregar_sin_repetidos(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento}")
        else:
            lista.append(elemento)
    except ValueError as e:
        print(e)

elementos = [3, 5, 10]

agregar_sin_repetidos(elementos, 7)
agregar_sin_repetidos(elementos, "Python")
agregar_sin_repetidos(elementos, 5)

print(elementos)

''''''En esta función, primero se verifica si el elemento ya está en la lista usando la expresión 
      "elemento in lista". Si el elemento está en la lista, se lanza una excepción "ValueError" 
    con un mensaje personalizado. Si el elemento no está en la lista, se agrega al final 
    de la misma.'''''

6) Busca en la documentación otra excepción que no se haya utilizado hasta ahora y realiza los siguientes pasos:
* Provoca el error en un código de ejemplo. 
* Una vez que las hayas provocado, contrólalas con try-except
* Muestra al usuario la información por defecto que proporcione la excepción. Pista: as
* Personaliza el mensaje que se le proporciona al usuario utilizando todo lo anterior
#Provocar el error en un código de ejemplo y Controlar la excepción con try-except:
try:
    archivo = open("archivo_que_no_existe.txt", "r")
except FileNotFoundError:
    print("Se produjo un FileNotFoundError al intentar abrir el archivo.")

Se produjo un FileNotFoundError al intentar abrir el archivo.

#Mostrar al usuario la información por defecto que proporcione la excepción utilizando as:
try:
    archivo = open("archivo_que_no_existe.txt", "r")
except FileNotFoundError as e:
    print("Se produjo un FileNotFoundError:", e)

Se produjo un FileNotFoundError: [Errno 2] No such file or directory: 'archivo_que_no_existe.txt'

#Personalizar el mensaje que se le proporciona al usuario utilizando todo lo anterior:
try:
    archivo = open("archivo_que_no_existe.txt", "r")
except FileNotFoundError as e:
    print("Error: El archivo 'archivo_que_no_existe.txt' no se pudo encontrar.")
    print("Información detallada:", e)

Error: El archivo 'archivo_que_no_existe.txt' no se pudo encontrar.
Información detallada: [Errno 2] No such file or directory: 'archivo_que_no_existe.txt'












