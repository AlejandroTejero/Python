from dispositivos import Procesador


class ProcesadorUpper(Procesador):
    def procesar(self, datos: str):
        self.salida.procesar(datos.upper())


class ProcesadorRever(Procesador):
    def procesar(self, datos: str):
        self.salida.procesar(datos[::-1])
