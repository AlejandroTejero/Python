def imprimir_num_centrales_inversos(lista1,lista2):
    lista1.extend(lista2)
    print(lista1)
    n = len(lista1)
    n_centrales = n // 2

    i_inicial = (n-n//2)//2
    i_final = i_inicial + n_centrales
    lista_centrales =lista1[i_inicial:i_final]

    print(lista_centrales[::-1])

lista1 = [1,2,3]
lista2 = [4,5,6]

imprimir_num_centrales_inversos(lista1,lista2)
