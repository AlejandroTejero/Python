def sift(lista, divisor):
    result = []
    for numeros in lista:
        if numeros % divisor != 0:
            result.append(numeros)

    return result

print(sift([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))