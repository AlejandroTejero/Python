#Ejercicio4
class coches:
    def __init__(self,marca,modelo,anio_matriculacion,ultima_itv):
        self.marca = marca
        self.modelo = modelo
        self.anio_matriculacion = anio_matriculacion
        self.ultima_itv = ultima_itv

    #def pintar_coche(self):
    def toca_itv(self):
        matriculacion = (2023 - self.anio_matriculacion)
        if matriculacion < 4:
            print(f" El coche es {self.marca}, {self.modelo} no debe")
        elif 4 <= matriculacion <= 10 - self.ultima_itv == 1:
            print(f" El coche es {self.marca}, {self.modelo} cada dos años")
        elif 4 <= matriculacion <= 10 - self.ultima_itv != 1:
            print(f" El coche es {self.marca}, {self.modelo} pasarla en 2023")
        elif matriculacion > 10 - self.ultima_itv == 0:
            print(f" El coche es {self.marca}, {self.modelo} no debe pasarla en 2023")
        elif matriculacion > 10 and 2023 - self.ultima_itv != 0:
            print(f" El coche es {self.marca}, {self.modelo}  debe pasar en 2023")

coche = coches('audi','a4',2022,2020)

coche.toca_itv()

#Ejercicio5
'''class Dispositivo:
    def __init__(self,nombre):
    
    '''
