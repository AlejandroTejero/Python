import socket
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5556))
print(f"Cliente corriendo en {client_socket.getsockname()}")

try:
    while True:
        cancion = input('Introduzca la cancion: ')
        artista = input('Introduzca el artista: ')
        if artista == 'exit':
            print('Cliente cerrado por exit')
            break
        dicc = {'Cancion': {cancion}, 'Artista': {artista}}
        client_socket.sendall(pickle.dumps(dicc))

        lista_privada = pickle.loads(client_socket.recv(1024))
        print(f"Respuesta del servidor: {lista_privada}")
except KeyboardInterrupt:
    print('Cliente cerrado por Ctrl+C')

client_socket.close()
print('Cliente cerrado')