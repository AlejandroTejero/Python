try:
    inicio = 0
    salir = False
    while not salir:
        num = int(input('N:'))
        if num % 2 == 0:
            inicio += num
            if num == 0:
                salir = True
                print(inicio)
        else:
            salir = True
            print(f"El numero {num} no es par")

except ValueError:
    print('Introducir numero entero')
except TypeError:
    print('Introducir numero entero')