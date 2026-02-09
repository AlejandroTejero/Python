import pickle
import socket
import sys

puerto = int(sys.argv[1])
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),puerto))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

cliente_socket,client_address = server_socket.accept()
if cliente_socket:
    print(f"Nuevo cliente conectado con direccion {client_address}")
    nombre = cliente_socket.recv(1024).decode()
    print(f"Nombre recibido: {nombre}")

server_socket.close()
print("Servidor cerrado")





