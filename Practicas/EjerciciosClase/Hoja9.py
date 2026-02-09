familia = {"pepe": 3, "pepa": 10, "pepito": 1, "pepita": 25}
lista_vacia = []
def pet_lovers(familia):
    for dueno,mascota in familia.items():
        if mascota > 2:
            lista_vacia.append(dueno)

    return lista_vacia

print(pet_lovers(familia))