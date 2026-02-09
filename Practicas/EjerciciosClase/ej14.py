diccionario = {'a': 3, 'b': 4, 'c': 50, 'd': 1}

def obtener_max_min(d):
    return max(d.values()),min(d.values())

print(obtener_max_min(diccionario))
