import socket
import pickle

print('Para poder continuar con la conversacion con el cliente...')
numero = input('Introduzca un numero: ')

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5556))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

client_socket,client_address = server_socket.accept()
if client_socket:
    print(f"Cliente con direccion {client_address} conectado")
    client_socket.sendall(numero.encode())
    print(f"Numero: {numero} enviado")
    lista = pickle.loads(client_socket.recv(1024))
    print(f"La lista recibida es: {lista}")
