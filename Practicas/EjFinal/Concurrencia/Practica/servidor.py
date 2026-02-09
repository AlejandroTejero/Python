import socket
import threading
import pickle

uuids = {}
next_client_id = 1
cerrojo = threading.Lock()
def handle_client(client_socket,client_address):
    global uuids,cerrojo,next_client_id

    cerrojo.acquire()
    id = next_client_id
    uuids[client_address] = [id]
    next_client_id += 1
    client_socket.sendall(pickle.dumps(id))
    cerrojo.release()

    print(f"Cliente {id} ({client_address}) conectado")
    while True:
        msg = client_socket.recv(1024)
        if not msg:
            print(f"Cliente ({client_address}) cerrado")
            client_socket.close()
            break
        mensaje = msg.decode()
        print(f"El mensaje recibido es {mensaje}")
        client_socket.sendall(mensaje.encode().upper())

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5555))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

try:
    while True:
        client_socket,client_address = server_socket.accept()
        t = threading.Thread(target=handle_client
                             ,args=[client_socket,client_address])
        t.start()
except KeyboardInterrupt:
    print('Servidor cerrado con Ctrl + C')

server_socket.close()