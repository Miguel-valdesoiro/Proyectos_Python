Ejercicio nº3:

class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__tipo = tipo
        print(f"Producto '{self.__nombre}' creado con éxito.")

    def __str__(self):
        return f"Código: {self.__codigo}, Nombre: {self.__nombre}, Precio: {self.__precio}, Tipo: {self.__tipo}"

    @property
    def codigo(self):
        '''Metodo getter del atributo codigo'''
        return self.__codigo

    @property
    def nombre(self):
        '''Metodo getter del atributo nombre'''
        return self.__nombre

    @property
    def precio(self):
        '''Metodo getter del atributo precio'''
        return self.__precio

    @property
    def tipo(self):
        '''Metodo getter del atributo tipo'''
        return self.__tipo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        '''Metodo setter del atributo codigo'''
        self.__codigo = nuevo_codigo

    @nombre.setter
    def nombre(self, nuevo_nombre):
        '''Metodo setter del atributo nombre'''
        self.__nombre = nuevo_nombre

    @precio.setter
    def precio(self, nuevo_precio):
        '''Metodo setter del atributo precio'''
        self.__precio = nuevo_precio

    @tipo.setter
    def tipo(self, nuevo_tipo):
        '''Metodo setter del atributo tipo'''
        self.__tipo = nuevo_tipo
        
# Crear algunos productos
producto1 = Producto("P001", "Camiseta", 20.99, "Ropa")
producto2 = Producto("P002", "Zapatillas", 59.99, "Calzado")

# Mostrar la información de los productos usando el método __str__
print(producto1)
print(producto2)

# Acceder a los atributos a través de los métodos getter
print(producto1.codigo)  # Imprimirá "P001"
print(producto1.nombre)  # Imprimirá "Camiseta"
print(producto1.precio)  # Imprimirá 20.99
print(producto1.tipo)    # Imprimirá "Ropa"

# Modificar los atributos a través de los métodos setter
producto1.codigo = "P003"
producto1.nombre = "Pantalón"
producto1.precio = 34.99
producto1.tipo = "Ropa deportiva"

# Mostrar la información actualizada usando el método __str__
print(producto1)  # Imprimirá "Código: P003, Nombre: Pantalón, Precio: 34.99, Tipo: Ropa deportiva"