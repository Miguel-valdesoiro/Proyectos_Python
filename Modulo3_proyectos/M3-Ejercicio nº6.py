M3_Ejercicio nº6:

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
        return f"{super().__str__()}\nVelocidad: {self.velocidad} km/h\nCilindrada: {self.cilindrada} cc"

# Ejemplo de uso
coche1 = Coche("Rojo", 4, 200, 1600)
coche2 = Coche("Azul", 4, 180, 2000)

print("Información del Coche 1:")
print(coche1)

print("\nInformación del Coche 2:")
print(coche2)
