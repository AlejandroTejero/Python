productos = [
    {'nombre': "Portátil", 'precio': 799.99, 'cantidad': 10},
    {'nombre': "Bolígrafo", 'precio': 1, 'cantidad': 0},
    {'nombre': "Tablet", 'precio': 250, 'cantidad': 20},
    {'nombre': "Teléfono", 'precio': 1250, 'cantidad': 5},
    {'nombre': "Calefactor", 'precio': 20, 'cantidad': 0},
]

def calcular_valor_total(productos):
    total = 0
    for producto in productos:
        total += producto['precio'] * producto['cantidad']
    return total

def imprimir_producto(producto):
    print(f"{producto['nombre']} ({producto['cantidad']}): {producto['precio']} €")


def esta_agotado(producto):
    return producto['cantidad'] == 0


def imprimir_inventario(productos):
    for producto in productos:
        if not esta_agotado(producto):
            imprimir_producto(producto)


def imprimir_productos_agotados(productos):
    for producto in productos:
        if esta_agotado(producto):
            imprimir_producto(producto)


print(calcular_valor_total(productos))
imprimir_inventario(productos)
imprimir_productos_agotados(productos)
