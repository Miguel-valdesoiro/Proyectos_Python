M3_Ejercicio nº4:

class Producto:
    def __init__(self, nombre, precio, descripcion, stock):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock

    def __str__(self):
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\nDescripción: {self.descripcion}\nStock: {self.stock}"

    def calcular_total(self, cantidad):
        if cantidad <= self.stock:
            return self.precio * cantidad
        else:
            return 0

# Ejemplo de uso
producto1 = Producto("Camisa", 25, "Camisa de algodón", 10)

print(producto1)  # Imprime los detalles del producto
print("Precio total (5 unidades):", producto1.calcular_total(5))
