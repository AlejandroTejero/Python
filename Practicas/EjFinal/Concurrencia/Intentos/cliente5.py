import socket
import pickle


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5556))
print(f"Cliente  con direccion {client_socket.getsockname()} corriendo")

try:
    while True:
        frase = input('Introduzca frase: ')
        if frase == 'bye bye':
            print('Cliente cerrado por bye bye')
            break
        client_socket.sendall(pickle.dumps(frase))
        frase_mayusculas = pickle.loads(client_socket.recv(1024))
        print(f"La frase obtenida es: {frase_mayusculas}")
except KeyboardInterrupt:
    print('Cliente cerrado por Ctrl+C')

client_socket.close()