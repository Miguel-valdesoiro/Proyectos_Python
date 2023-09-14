Ejercicio nº1:

Ejeclass Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"Alumno '{self.nombre}' creado con éxito.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}"

    def calificacion(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha suspendido.")
            
# Crear algunos alumnos
alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("Maria", 4)
alumno3 = Alumno("Carlos", 6)

# Mostrar la información de los alumnos usando el método __str__
print(alumno1)
print(alumno2)
print(alumno3)

# Mostrar la calificación de los alumnos usando el método calificacion
alumno1.calificacion()
alumno2.calificacion()
alumno3.calificacion()





