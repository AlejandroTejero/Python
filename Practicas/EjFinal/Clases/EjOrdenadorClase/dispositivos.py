class Dispositivo:
    def __init__(self, n):
        self.nombre = n


class Entrada(Dispositivo):
    def __init__(self, n):
        super().__init__(n)
        self.procesador = None

    def procesar(self):
        cad = input("Introduzca una cadena: ")
        self.procesador.procesar(cad)

    def conectar_a(self, proc):
        self.procesador = proc


class Salida(Dispositivo):
    def procesar(self, cad: str):
        print(cad)


class Procesador(Dispositivo):
    def __init__(self, n):
        super().__init__(n)
        self.salida = None

    def procesar(self, datos: str):
        self.salida.procesar(datos)

    def conectar_a(self, sal):
        self.salida = sal
