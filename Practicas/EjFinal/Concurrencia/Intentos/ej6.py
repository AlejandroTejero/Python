import threading

lista_compartida = []
cerrojo = threading.Lock()

def f():
    global lista_compartida

    cerrojo.acquire()
    for i in range(1,6):
        lista_compartida.append(i)
    cerrojo.release()

try:
    for i in range(3):
        t = threading.Thread(target=f,args=[])
        t.start()
except KeyboardInterrupt:
    print('Cerrado por Ctrl+C')

print(lista_compartida)