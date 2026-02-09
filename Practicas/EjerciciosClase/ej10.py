def imprimir_numeros_centrales_inversos(l1, l2):
    lc = l1 + l2
    n = len(lc)
    middle = n // 2
    begin = (n - middle) // 2
    end = begin + middle
    print(lc[begin:end][::-1])


imprimir_numeros_centrales_inversos([1, 2, 3], [4, 5, 6, 7])
imprimir_numeros_centrales_inversos([9, 8, 7, 6], [5, 4, 3, 2])
