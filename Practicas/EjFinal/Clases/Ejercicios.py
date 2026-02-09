'Ejercicio 1,2 y 3'
'''class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def pintar_producto(self):
        print(self.nombre, self.precio)

Producto1 = Producto('Papel',20)
Producto1.pintar_producto()'''

'Ejercicio 4,5 y 6'
'''class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def pintar_producto(self):
        print(self.nombre, self.precio)

class Cliente:
    def __init__(self,nombre,correo):
        self.nombre = nombre
        self.correo = correo
        self.cesta_compra = []

    def anadir_cesta(self,producto):
        self.cesta_compra.append(producto)

    def pintar_productos(self):
        dicc = []
        for producto in self.cesta_compra:
            dicc.append({'Nombre': producto.nombre, 'Precio': producto.precio})
        return dicc
    def calcular_valor_total(self):
        total = 0
        for producto in self.cesta_compra:
            total += producto.precio
        return f"El precio total es: {total}"

class ClienteVIP(Cliente):
    def __init__(self,nombre,correo,descuento = 10):
        super().__init__(nombre,correo)
        self.descuento = descuento

    def calcular_valor_total(self):
        total = 0
        for producto in self.cesta_compra:
            total += producto.precio - (producto.precio * self.descuento)/100
        return total


Cliente1 = Cliente('Pepito','pepito03')
Cliente2 = ClienteVIP('Alejandro','alejandro03',15)


Producto1 = Producto('Papel',20)
Producto2 = Producto('Agua',5)
Producto3 = Producto('Lejia',20)
Producto4 = Producto('Vino',6)


Cliente1.anadir_cesta(Producto1)
Cliente1.anadir_cesta(Producto2)
Cliente2.anadir_cesta(Producto3)
Cliente2.anadir_cesta(Producto4)

print('Cliente1:')
print(Cliente1.pintar_productos())
print(Cliente1.calcular_valor_total())
print('Cliente2:')
print(Cliente2.pintar_productos())
print(Cliente2.calcular_valor_total())'''

'Ejercicio ITV'
'''anio_actual= 2024
class Coche:
    def __init__(self,marca,modelo,anio_matriculacion,ultima_itv):
        self.marca = marca
        self.modelo = modelo
        self.anio_matriculacion = anio_matriculacion
        self.ultima_itv = ultima_itv

    def toca_itv(self):
        if self.anio_matriculacion - anio_actual < 4:
            print(f"El coche {self.marca} {self.modelo} no debe pasar la itv")
        elif 4 <= self.anio_matriculacion - anio_actual <= 10:
            print(f"El coche {self.marca} {self.modelo} debe pasar la itv cada 2 años")
        elif  self.anio_matriculacion - anio_actual > 10:
            print(f"El coche {self.marca} {self.modelo} debe pasar la itv cada año")


coche1 = Coche('Kia','Rio',2019,2022)
coche1.toca_itv()'''

