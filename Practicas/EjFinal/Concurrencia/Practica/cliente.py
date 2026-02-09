import socket
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5555))

id = pickle.loads(client_socket.recv(1024))
print(f"Cliente {id} corriendo en: {client_socket.getsockname()}")

try:
    while True:
        frase = input('Introduzca frase: ')
        if frase == 'exit':
            print('Cliente cerrado por exit')
            break
        client_socket.sendall(frase.encode())
        frase_de_vuelta = client_socket.recv(1024).decode()
        print(f"Frase en MAYUSCULAS: {frase_de_vuelta}")
except KeyboardInterrupt:
    print('Cliente cerrado con Ctrl + C')

client_socket.close()