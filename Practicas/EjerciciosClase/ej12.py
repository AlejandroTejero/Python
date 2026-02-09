diccionario = {'a': 3,'b':4,'c':5}

def suma_valores(d):
    suma = 0
    for i in d.values():
        suma += i
    return suma

print(suma_valores(diccionario))


for i in diccionario.values():
    print(i)
for j in diccionario.keys():
    print(j)
for k,y in diccionario.items():
    print(k,y)

