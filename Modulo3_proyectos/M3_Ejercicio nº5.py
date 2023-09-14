M3_Ejercicio nº5:

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


class Pedido:
    def __init__(self, productos, cantidades):
        self.productos = productos
        self.cantidades = cantidades
        print("¡Pedido creado con éxito!")

    def total_pedido(self):
        total = 0
        for producto, cantidad in zip(self.productos, self.cantidades):
            total += producto.calcular_total(cantidad)
        return total

    def mostrar_pedido(self):
        print("Productos en el pedido:")
        for producto, cantidad in zip(self.productos, self.cantidades):
            print(f"{producto.nombre} - Cantidad: {cantidad}")

# Ejemplo de uso
producto1 = Producto("Camisa", 25, "Camisa de algodón", 10)
producto2 = Producto("Pantalón", 40, "Pantalón de mezclilla", 5)
producto3 = Producto("Zapatos", 60, "Zapatos de cuero", 8)

productos_pedido = [producto1, producto2, producto3]
cantidades_pedido = [2, 1, 3]

pedido1 = Pedido(productos_pedido, cantidades_pedido)
print("Total del pedido:", pedido1.total_pedido())
pedido1.mostrar_pedido()
