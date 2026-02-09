import random

def funcion(x: float)-> float:
    y = x
    return y

def calcular_area(func,max_iteraciones:int,max_x:float,max_y:float):
    coordenadas_dentro = 0
    for intento in range(0,max_iteraciones):
        muestra_x = random.random() * max_x
        muestra_y = random.random() * max_y
        if muestra_y < func(muestra_x):
            coordenadas_dentro += 1
        area = (coordenadas_dentro / max_iteraciones) * max_x * max_y
        return area

print(calcular_area(funcion,200000,0,1))