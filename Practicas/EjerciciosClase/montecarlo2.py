import random

def calcular_area(f,iteraciones,area_exposicion):
    x_max, y_max = area_exposicion
    puntos_dentro = 0
    for _ in range(iteraciones):
        x = random.uniform(0, x_max)
        y = random.uniform(0, y_max)

        if y < f(x):
            puntos_dentro += 1

    return (puntos_dentro / iteraciones) * (x_max * y_max)


def g(x):
    return x ** 2


iteraciones = 10
area_exposicion = (1,1)
area = calcular_area(g,iteraciones,area_exposicion)

print(f" Area bajo la curva: {area}")
