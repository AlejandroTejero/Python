import socket
import sys

ip = sys.argv[1]
puerto = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip,puerto))
print(f"Cliente corriendo en {client_socket.getsockname()}")

nombre = input('Introduzca su nombre: ')
client_socket.sendall(nombre.encode())

client_socket.close()
print("Cliente cerrado")