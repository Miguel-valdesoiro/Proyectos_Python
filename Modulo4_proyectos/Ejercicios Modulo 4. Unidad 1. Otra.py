 Ejercicios Modulo 4. Unidad 1. Otras herramientas de POO (Soluciones)

Ejercicio nº1:

class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def repostar(self):
        print("Este vehiculo tiene que repostar gasolina")

class VElectricos:
    def __init__(self, marca, modelo, autonomia):
        self.marca = marca
        self.modelo = modelo
        self.autonomia = autonomia

    def repostar(self):
        print("Este vehiculo tiene que repostar electricidad")

class BicicletaElectrica(VElectricos, Vehiculos):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo, autonomia)

class Quad(Vehiculos, VElectricos):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia

# Crear objetos
bicicleta_electrica = BicicletaElectrica("BiciElec", "Modelo1", 50)
quad = Quad("QuadElec", "Modelo2", 100)

# Utilizar el polimorfismo para llamar al método repostar
vehiculos = [bicicleta_electrica, quad]

for vehiculo in vehiculos:
    vehiculo.repostar()

Ejercicio nº2:

class Personal_Universitario:
    def __init__(self, id, nombre, email):
        self.datos = {
            "id": id,
            "nombre": nombre,
            "email": email
        }

    def mostrar_informacion(self):
        print("Información del Personal Universitario:")
        for key, value in self.datos.items():
            print(f"{key}: {value}")
        print("\n")

class Oficina(Personal_Universitario):
    def __init__(self, id, nombre, email, puesto):
        super().__init__(id, nombre, email)
        self.datos["Puesto"] = puesto

    def mostrar_informacion(self):
        print("Información de la Oficina:")
        for key, value in self.datos.items():
            print(f"{key}: {value}")
        print("\n")

class Profesor(Personal_Universitario):
    def __init__(self, id, nombre, email, especializacion):
        super().__init__(id, nombre, email)
        self.datos["Especialización"] = especializacion

    def mostrar_informacion(self):
        print("Información del Profesor:")
        for key, value in self.datos.items():
            print(f"{key}: {value}")
        print("\n")

class Alumno(Personal_Universitario):
    def __init__(self, id, nombre, email, creditos_aprobados):
        super().__init__(id, nombre, email)
        self.datos["Créditos Aprobados"] = creditos_aprobados

    def mostrar_informacion(self):
        print("Información del Alumno:")
        for key, value in self.datos.items():
            print(f"{key}: {value}")
        print("\n")

# Crear objetos de cada clase
oficina = Oficina("123", "Juan Perez", "juan@example.com", "Secretario")
profesor = Profesor("456", "Maria Rodriguez", "maria@example.com", "Matemáticas")
alumno = Alumno("789", "Luis Gonzalez", "luis@example.com", 120)

# Mostrar información de los objetos
oficina.mostrar_informacion()
profesor.mostrar_informacion()
alumno.mostrar_informacion()

Ejercicio nº3:

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"{self.marca} {self.modelo}"

class Terrestre(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas):
        super().__init__(marca, modelo)
        self.num_ruedas = num_ruedas

    def describir(self):
        return f"{super().describir()} - {self.num_ruedas} ruedas"

class Electrico(Terrestre):
    def __init__(self, marca, modelo, num_ruedas, autonomia):
        super().__init__(marca, modelo, num_ruedas)
        self.autonomia = autonomia

    def describir(self):
        return f"{super().describir()} - Autonomía: {self.autonomia} km"

class BicicletaElectrica(Electrico):
    def __init__(self, marca, modelo, num_ruedas, autonomia):
        super().__init__(marca, modelo, num_ruedas, autonomia)

class Moto(Terrestre):
    def __init__(self, marca, modelo, num_ruedas, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.cilindrada = cilindrada

    def describir(self):
        return f"{super().describir()} - Cilindrada: {self.cilindrada} cc"

# Crear objetos
bicicleta_electrica = BicicletaElectrica("Tesla", "eBike", 2, 80)
moto_gasolina = Moto("Honda", "CBR1000RR", 2, 1000)

# Mostrar información usando polimorfismo
vehiculos = [bicicleta_electrica, moto_gasolina]

for vehiculo in vehiculos:
    print(vehiculo.describir())