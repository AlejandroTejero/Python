import pickle
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5555))
server_socket.listen(1)
print(f"Escuchando en {server_socket.getsockname()}")

lista_vacia = {}
while True:
    print('Escuchando...')
    client_socket,client_address = server_socket.accept()
    if client_socket:
        print(f"Cliente {client_address} conectado")
        while True:
            msg = client_socket.recv(1024)
            if not msg:
                print(f"conexion con {client_address} cerrada")
                break
            data = pickle.dumps(msg)
            print(f"Datos recibidos: {data}")
            lista_vacia.append(data)
            client_socket.sendall(pickle.loads(lista_vacia))

'''import socket
import pickle

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5555))
server_socket.listen()
print(f"Conectando con direccion {server_socket.getsockname()}")


lista_vacia = []
while True:
    client_socket,client_address = server_socket.accept()
    if client_socket:
        print(f"Conectado con {client_address}")
        while True:
            msg = client_socket.recv(1024)
            if not msg:
                print('No existe mensaje')
                break
            str_msg = pickle.loads(msg)
            print(f"Mensaje recibido: {str_msg}")
            lista_vacia.append(str_msg)
            client_socket.sendall(pickle.dumps(lista_vacia))'''
