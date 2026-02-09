import threading

MIN_NUMERO = 1
MAX_NUMERO = 5
N_THREADS = 3

variable_compartida = []
cerrojo = threading.Lock()


def f():
    global variable_compartida, cerrojo

    cerrojo.acquire()
    for n in range(MIN_NUMERO, MAX_NUMERO + 1):
        variable_compartida.append(n)
    cerrojo.release()


for _ in range(N_THREADS):
    t = threading.Thread(target=f)
    t.start()

print(variable_compartida)