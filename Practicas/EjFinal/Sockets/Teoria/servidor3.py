import pickle
import socket
lista_vacia = []
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5555))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

client_socket,client_address = server_socket.accept()
if client_socket:
    print(f"Cliente {client_address} conectado")
    while True:
        mensaje = pickle.loads(client_socket.recv(1024))
        if not mensaje:
            break
        print(f"Diccionario recibido: {mensaje}")
        lista_vacia.append(mensaje)
        client_socket.sendall(pickle.dumps(lista_vacia))

