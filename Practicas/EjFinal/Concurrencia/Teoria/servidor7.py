import socket
import threading
import pickle

lista_privada = {}
cerrojo = threading.Lock()
def handle_client(client_socket,client_address):
    global lista_privada, cerrojo

    print(f"Cliente {client_address} conectado")
    if client_socket:
        while True:
            dicc = pickle.loads(client_socket.recv(1024))
            if not dicc:
                client_socket.close()
                print(f"Cliente con direccion ({client_address}) cerrado")
                break
            print(f"Los datos recibidos son: {dicc}")
            cerrojo.acquire()
            if client_address in lista_privada:
                lista_privada[client_address].append(dicc)
            else:
                lista_privada[client_address] = [dicc]
            cerrojo.release()
            client_socket.sendall(pickle.dumps(lista_privada[client_address]))

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5556))
server_socket.listen()
print(f"Servidor escuchando en {server_socket.getsockname()}")

try:
    while True:
        client_socket,client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client,args=[client_socket,client_address])
        thread.start()
except KeyboardInterrupt:
    server_socket.close()
    print('Servidor cerrado por  Ctrl+C')