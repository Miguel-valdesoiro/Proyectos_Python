M3_Ejercicio nº7:

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
        return f"{type(self).__name__}\n{super().__str__()}\nVelocidad: {self.velocidad} km/h\nCilindrada: {self.cilindrada} cc"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{type(self).__name__}\n{super().__str__()}\nTipo: {self.tipo}"


class Camion(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga

    def __str__(self):
        return f"{type(self).__name__}\n{super().__str__()}\nCarga: {self.carga} ton"


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


# Ejemplo de uso
coche1 = Coche("Rojo", 4, 200, 1600)
coche2 = Coche("Azul", 4, 180, 2000)
bicicleta1 = Bicicleta("Verde", 2, "Montaña")
camion1 = Camion("Gris", 6, 10)

lista_vehiculos = [coche1, coche2, bicicleta1, camion1]

catalogar(lista_vehiculos)
catalogar(lista_vehiculos, 4)
