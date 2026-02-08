no_leer = False
lista_vacia = []
suma = 0
while not no_leer:
    try:
        num = int(input('Introdir numero entero: '))
        if (num != 0):
            if num > 0:
                lista_vacia.append(num)
                suma += num
        else:
            no_leer = True
    except ValueError:
        print('Solo numeros enteros')
    except TypeError:
        print('[ERROR')

print(lista_vacia)
print(suma)