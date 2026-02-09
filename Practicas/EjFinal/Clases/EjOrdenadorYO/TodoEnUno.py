class Dispositivo:
    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Entrada(Dispositivo):
    def __init__(self,nombre):
        super().__init__(nombre)
    def conectar_a(self,procesador):
        print(f"Conectando {self.nombre} a {procesador}...")
        self.procesador = procesador

    def procesar(self):
        if self.procesador is not None:
            s = input("Cadena de caracteres: ")
            self.procesador.procesar(s)
        else:
            print("No se puede procesar")

class Procesador(Dispositivo):
    def __init__(self,nombre):
        super().__init__(nombre)

    def conectar_a(self,salida):
        print(f"Conectando {self.nombre} a {salida}...")
        self.salida = salida

    def procesar(self, s):
        if self.salida is not None:
            self.salida.procesar(s)
        else:
            print("No se puede procesar")

class Salida(Dispositivo):
    def __init__(self,nombre):
        super().__init__(nombre)

    def procesar(self, s):
        print(f"{self.nombre}: {s}")



class ProcesadorUpper(Procesador):
    def __init__(self,nombre):
        super().__init__(nombre)
    def procesar(self,s):
        if self.salida is not None:
            self.salida.procesar(s).upper()
        else:
            print("No se puede procesar")



class ProcesadorRever(Procesador):
    def __init__(self,nombre):
        super().__init__(nombre)
    def procesar(self,s):
        if self.salida is not None:
            self.salida.procesar(s[::-1])
        else:
            print("No se puede procesar")

