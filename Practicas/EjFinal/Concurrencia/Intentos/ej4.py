import time
import threading

def siesta(indice):
    time.sleep(1)
    print(f"{indice}: se ha despertado de la siesta")

for i in range(9):
    thread = threading.Thread(target=siesta,args=[i])
    thread.start()