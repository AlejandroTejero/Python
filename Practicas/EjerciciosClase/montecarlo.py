import random


def calcular_area(f, iteraciones, area_exposicion):
    max_x, max_y = area_exposicion
    puntos_bajo_curva = 0
    for _ in range(iteraciones):
        x = random.uniform(0, max_x)
        y = random.uniform(0, max_y)

        if y <= f(x):
            puntos_bajo_curva += 1

    return (puntos_bajo_curva / iteraciones) * (max_x * max_y)


def g1(x):
    return x ** 2

iteraciones = 10
area_exposicion = (1, 1)

area = calcular_area(g1, iteraciones, area_exposicion)
print(f"Área aproximada bajo la curva: {area}")