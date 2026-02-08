lista_vacia = []

salir = False
while not salir:
    try:
        num = int(input("N: "))
        if num == 0:
            salir = True
        else:
            lista_vacia.append(num)
    except ValueError:
        print("[ERROR]: debes introducir un número entero")

salir = False
while not salir:
    entrada = input("Num: ")
    if entrada == "exit":
        salir = True
    else:
        try:
            num = int(entrada)
            if num in lista_vacia:
                lista_vacia.remove(num)
        except ValueError:
            print("[ERROR]: debes introducir un número entero o el comando 'exit'")

print(lista_vacia)