class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

kilo_peras = Producto('peras',1.99)
kilo_manzanas = Producto('manzanas',3.4)
print(kilo_peras.precio)
print(kilo_manzanas.nombre)