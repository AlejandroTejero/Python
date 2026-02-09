import socket
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5556))
print(f"Cliente corriendo con direccion {client_socket.getsockname()}")

numero = client_socket.recv(1024).decode()
print(f"Numero recibido es: {numero}")

n1 = 1 ** int(numero)
n2 = 2 ** int(numero)
n3 = 3 ** int(numero)

lista = f"(1,{n1}),(2,{n2}),(3,{n3})"
client_socket.sendall(pickle.dumps(lista))
print(f"Lista ({lista}) enviada")