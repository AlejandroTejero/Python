from dispositivos import Salida


class EscribirFichero(Salida):
    def procesar(self, cad: str):
        with open("procesado.txt", "w") as f:
            f.writelines(cad)
