import time
import threading

N = 10

def siesta(indice):
    time.sleep(1)
    print(f"{indice}: se ha despertado de la siesta")

for i in range(0,N):
    t = threading.Thread(target=siesta,args=[i])
    t.start()


'Javi'
'''import threading
import time

N = 10


def siesta(indice):
    time.sleep(1)
    print(f"El hilo {indice} se ha despertado de la siesta")


for i in range(N):
    t = threading.Thread(target=siesta, args=[i])  # args=(i,)
    t.start()'''
