'Ejercicio Ordenadores'
class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre


class Entrada(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.procesador = None

    def procesar(self):
        cadena_carateres = input(f"Ingrese datos para el dispositivo {self.nombre}")
        self.procesador.procesar(cadena_carateres)

    def conectar_a(self,procesador):
        self.procesador = procesador

class Procesador(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.salida = None

    def procesar(self,datos=str):
        self.salida.procesar(datos)

    def conectar_a(self,salida):
        self.salida = salida


class Salida(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def procesar(self,cad=str):
        print(cad)
