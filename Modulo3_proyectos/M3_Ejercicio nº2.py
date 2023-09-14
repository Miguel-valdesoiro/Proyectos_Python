
Ejercicio nº2:
class Alumno:
    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota
        print(f"Alumno '{self.__nombre}' creado con éxito.")

    def __str__(self):
        return f"Nombre: {self.__nombre}, Nota: {self.__nota}"

    def calificacion(self):
        if self.__nota >= 5:
            print(f"{self.__nombre} ha aprobado.")
        else:
            print(f"{self.__nombre} ha suspendido.")

    @property
    def nombre(self):
        '''Metodo getter del atributo nombre'''
        return self.__nombre

    @property
    def nota(self):
        '''Metodo getter del atributo nota'''
        return self.__nota

    @nombre.setter
    def nombre(self, nuevo):
        '''Metodo setter del atributo nombre'''
        self.__nombre = nuevo

    @nota.setter
    def nota(self, nuevo):
        '''Metodo setter del atributo nota'''
        self.__nota = nuevo


# Crear un alumno
alumno1 = Alumno("Juan", 7)

# Intentar acceder directamente a las variables (esto generaría un error)
# print(alumno1.__nombre)  # Generará AttributeError: 'Alumno' object has no attribute '__nombre'
# print(alumno1.__nota)    # Generará AttributeError: 'Alumno' object has no attribute '__nota'

# Acceder a las variables a través de los métodos getter
print(alumno1.nombre)  # Imprimirá "Juan"
print(alumno1.nota)    # Imprimirá 7

# Modificar las variables a través de los métodos setter
alumno1.nombre = "Pedro"
alumno1.nota = 5

# Mostrar la información actualizada usando el método __str__
print(alumno1)  # Imprimirá "Nombre: Pedro, Nota: 5"

# Mostrar la calificación actualizada usando el método calificacion
alumno1.calificacion()  # Imprimirá "Pedro ha aprobado.