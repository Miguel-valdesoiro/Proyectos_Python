M3_Ejercicio nº8:

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}\nRuedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Coche\n{super().__str__()}\nVelocidad: {self.velocidad} km/h\nCilindrada: {self.cilindrada} cc"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta\n{super().__str__()}\nTipo: {self.tipo}"


class Camion(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

    def __str__(self):
        return f"Camión\n{super().__str__()}\nCarga: {self.carga} ton"


def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtered_vehicles = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(filtered_vehicles)} vehículos con {ruedas} ruedas:")
        for vehiculo in filtered_vehicles:
            print(vehiculo)
    else:
        for vehiculo in vehiculos:
            print(vehiculo)
        print("\n")


def filtrar(vehiculos, tipo_vehiculo):
    vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if isinstance(vehiculo, tipo_vehiculo)]
    return vehiculos_filtrados


# Ejemplo de uso
coche1 = Coche("Rojo", 4, 200, 1600)
coche2 = Coche("Azul", 4, 180, 2000)
bicicleta1 = Bicicleta("Verde", 2, "Montaña")
bicicleta2 = Bicicleta("Blanca", 2, "Ciudad")
camion1 = Camion("Gris", 6, 10)
camion2 = Camion("Azul", 6, 8)

lista_vehiculos = [coche1, coche2, bicicleta1, bicicleta2, camion1, camion2]

# Filtrar por tipo de vehículo
lista_coches = filtrar(lista_vehiculos, Coche)
lista_bicicletas = filtrar(lista_vehiculos, Bicicleta)
lista_camiones = filtrar(lista_vehiculos, Camion)

print("Lista de Coches:")
catalogar(lista_coches)

print("Lista de Bicicletas:")
catalogar(lista_bicicletas)

print("Lista de Camiones:")
catalogar(lista_camiones)
