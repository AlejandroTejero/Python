'''edades = {"0": 15, "1": 3, "2": 57, "3": 22, "4": 58}

def older(diccionario):
    result = None
    edad_base = 0
    for dni,edad in diccionario.items():
        if edad > edad_base:
            edad_base = edad
            result = dni
    return result

print(older(edades))


edades = {"0": 15, "1": 3, "2": 58, "3": 22, "4": 58}

def older(diccionario):
    result = None
    max_edad = None
    for dni,edad in diccionario.items():
        if not max_edad or edad > max_edad:
            result = dni
            max_edad = edad
    return result

print(older(edades))'''

'''salir = False
lista_vacia = []

while not salir:
    try:
        num = int(input('Introducir numero: '))
        if num == 0:
            salir = True
        else:
            lista_vacia.append(num)
    except ValueError:
        print('[ERROR : NUMERO ENTERO]')

salir = False
while not salir:
        entrada = input('Introducir numero: ')
        if entrada.lower() == 'exit':
            salir = True
        else:
            try:
                n = int(entrada)
                if entrada in lista_vacia:
                    lista_vacia.remove(n)
            except ValueError:
                    print('INTRODUCIR EXIT')

print(lista_vacia)
'''

'''numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_vacia = []
divisor = 2

def sift(divisor):
    for num in numeros:
        if num % divisor != 0:
            lista_vacia.append(num)
    return lista_vacia

print(sift(divisor))'''

'''dias_semana = ['lunes','martes','miercoles']

for dias in dias_semana:
    for letras in dias:
        print(letras)
    print(dias_semana.index(dias)'''

'''dicc = {'a': 3, 'b': 4,'c':5}

def suma_valores(d):
    suma = 0
    for letras,valores in d.items():
        suma += valores
    return suma

print(suma_valores(dicc))'''

'''valores = {'x': "por", 'q': "que", '+': "más"}

def transformacion(texto):
    for letra,valor in valores.items():
        texto = texto.replace(letra,valor)

    return texto

with open('apuntes.txt','r') as fichero:
    texto = fichero.read()
    print(transformacion(texto))

with open('salida.txt','w') as salida:
    text = salida.write(texto)'''

'''productos = [
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
    print(f"{producto['nombre']},{producto['precio']} $, ({producto['cantidad']})")

def esta_agotado(productos):
    agotado = False
    for producto in productos:
        if producto['cantidad'] == 0:
            agotado = True

    return agotado

def imprimir_inventario(productos):
    for producto in productos:
        if not esta_agotado(productos):
            imprimir_producto(producto)

def imprimir_inventario_agotado(productos):
    for producto in productos:
        if esta_agotado(productos):
            imprimir_producto(producto)


print(calcular_valor_total(productos))
imprimir_inventario(productos)
imprimir_inventario_agotado(productos)'''

'''import random

def calcular_area(f,num_iteraciones,area_exposicion):
    puntos_bajo_curva = 0
    x_max, y_max = area_exposicion
    for _ in range(num_iteraciones):
        x = random.uniform(0, x_max)
        y = random.uniform(0, y_max)

        if y < f(x):
            puntos_bajo_curva += 1

    return (puntos_bajo_curva / num_iteraciones) * (x_max * y_max)

def g1(x):
    return x **2

num_iteraciones = 10
area_exposicion = (1,1)

print(calcular_area(g1,num_iteraciones,area_exposicion))'''

'''productos = [
    {'nombre': "Portátil", 'precio': 799.99, 'cantidad': 10},
    {'nombre': "Bolígrafo", 'precio': 1, 'cantidad': 0},
    {'nombre': "Tablet", 'precio': 250, 'cantidad': 20},
    {'nombre': "Teléfono", 'precio': 1250, 'cantidad': 5},
    {'nombre': "Calefactor", 'precio': 20, 'cantidad': 0}]

def calcular_valor_total(productos):
    total = 0
    for producto in productos:
        total += producto['precio'] * producto['cantidad']
    return total

def imprimir_producto(producto):
    print(f"{producto['nombre']}, {producto['precio']} $, ({producto['cantidad']})")

def imprimir_inventario_disponible(productos):
    for producto in productos:
        if producto['cantidad'] != 0:
            imprimir_producto(producto)
            
def imprimir_inventario_no_disponible(productos):
    for producto in productos:
        if producto['cantidad'] == 0:
            imprimir_producto(producto)

print(calcular_valor_total(productos))
imprimir_inventario_disponible(productos)
imprimir_inventario_no_disponible(productos)'''

'''abreviaturas = {'X':'por','Q':'que','Xq':'porque'}

def transformar(texto):
    for abreviatura,palabra in abreviaturas.items():
        texto = texto.replace(abreviatura,palabra)
    return texto

with open('apuntes.txt','r') as fichero:
    texto = fichero.read()
    print(transformar(texto))'''

'''num1 = 2
num2 = 1.1
division = num1 / num2

print(f"Resultado: {division:.1f}")'''

'''num_string = '12'
num_string = int(num_string)

print(num_string)'''

'''li = [1,2,3]
l2 = [4,5,6]

l1 = li + l2

print(l1)'''

'''def suma_dos_numeros(a, b):
 suma = a + b
 return suma

print(suma_dos_numeros(4, 4))'''

'''dicc = {'x': 'que', 'pq': 'porque'}

del dicc['pq']
dicc['cdo'] = 'cuando'
print(dicc)
print(dicc['x'])'''

'''abreviaturas = {'X':'por','Q':'que','Xq':'porque','Cdo':'cuando'}

def transformar(texto):
    for corto,largo in abreviaturas.items():
        texto = (texto.replace(corto,largo))
    return texto

with open('apuntes.txt','r') as fichero:
    texto = fichero.read()
    print(transformar(texto))
    
with open('salida.txt','w') as ficherosalida:
    ficherosalida.write(transformar(texto))'''

'''productos = [
    {'nombre': "Portátil", 'precio': 799.99, 'cantidad': 10},
    {'nombre': "Bolígrafo", 'precio': 1, 'cantidad': 0},
    {'nombre': "Tablet", 'precio': 250, 'cantidad': 20},
    {'nombre': "Teléfono", 'precio': 1250, 'cantidad': 5},
    {'nombre': "Calefactor", 'precio': 20, 'cantidad': 0},
]

def calcular_valor_total(productos):
    suma = 0
    for producto in productos:
        suma += producto['precio'] * producto['cantidad']
    return suma

def imprimir_producto(producto):
    print(f"{producto['nombre']}, {producto['precio']} $, ({producto['cantidad']})")
def imprimir_inventario_disponible(productos):
    for producto in productos:
        if producto['cantidad'] != 0:
            imprimir_producto(producto)
def imprimir_inventario_no_disponible(productos):
    for producto in productos:
        if producto['cantidad'] == 0:
            imprimir_producto(producto)

print(calcular_valor_total(productos))
print('Inventario disponible:')
imprimir_inventario_disponible(productos)
print('Inventario NO disponible:')
imprimir_inventario_no_disponible(productos)'''

'''productos = [
    {'nombre': "Portátil", 'precio': 799.99, 'cantidad': 10},
    {'nombre': "Bolígrafo", 'precio': 1, 'cantidad': 0},
    {'nombre': "Tablet", 'precio': 250, 'cantidad': 20},
    {'nombre': "Teléfono", 'precio': 1250, 'cantidad': 5},
    {'nombre': "Calefactor", 'precio': 20, 'cantidad': 0},
]

cocacola = {'nombre': 'CocaCola', 'precio': 10}
cocacola['cantidad'] = 15

productos.append(cocacola)
print(productos)'''

'''l1 = [1,2,3,4]


l3 = l1 + l2
l1.extend(l2)
l1.insert(0,5)
import random
x = random.uniform(0,5)

print(l1)'''


