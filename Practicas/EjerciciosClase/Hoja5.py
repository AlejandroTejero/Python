no_leer = False
Lista_vacia = []
suma = 0

while not no_leer:
    try:
        num = int(input('Introducir numero entero: '))
        if num != 0:
            Lista_vacia.append(num)
            suma += num
        else:
            no_leer = True
    except ValueError:
        print('[ERROR]')

print(Lista_vacia)
print(min(Lista_vacia))
print(max(Lista_vacia))
print(suma)
print(suma / 2)

