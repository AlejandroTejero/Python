import threading

lista = []
numero_threads = 3

cerrojo = threading.Lock()

def f():
    global lista, cerrojo

    cerrojo.acquire()
    for i in range(1,6):
        lista.append(i)
    cerrojo.release()


for i in range(numero_threads):
    thread = threading.Thread(target=f,args=[])
    thread.start()

print(lista)