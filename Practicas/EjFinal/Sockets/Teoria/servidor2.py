import socket
import sys

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5555))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

client_socket,client_address = server_socket.accept()
if client_socket:
    print(f"Cliente {client_address} conectado")
    while True:
        mensaje = client_socket.recv(1024).decode()
        if not mensaje:
            print("Servidor cerrado no hay mensaje")
            break
        print(f"Mensaje recibido {mensaje}")
        mensaje_upper = client_socket.sendall(mensaje.encode().upper())

server_socket.close()
print("Servidor Cerrado")