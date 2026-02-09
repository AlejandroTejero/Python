lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = 2


def sfit(lista):
    lista_vacia = []
    for num in lista:
        if num % divisor != 0:
            lista_vacia.append(num)

    return lista_vacia

print(sfit(lista))

