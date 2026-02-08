def agregar_tareas(lista_tareas,descripcion,prioridad):
    tarea = {'productos': descripcion, 'prioridad': prioridad}
    lista_tareas.append(tarea)
    return lista_tareas

def visualizar_tareas_prioritarias(lista_tarea):
    indice = 0
    for tarea in lista_tarea:
        if tarea['prioridad'] == 3:
            print(f"{indice}: {tarea['descripcion']}")
        indice += 1

#print(lista_tareas.index(tarea)) (para el indice, en vez de ir suamando 1)

lista_tareas = []
agregar_tareas(lista_tareas,'Hacer la compra',1)
agregar_tareas(lista_tareas,'Estudiar para el examen',3)
print(f"Total: {agregar_tareas(lista_tareas,'Llamar a Luis',2)}")

visualizar_tareas_prioritarias(lista_tareas)


