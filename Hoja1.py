try:
    Numero = int(input('introducir numero: '))
    restas = 0
    while Numero >= 2:
        Numero -= 2
        restas += 1
    print(f" Numero final: {Numero} , Numero de restas: {restas}")

except ValueError:
        print('Introducir numero entero')

