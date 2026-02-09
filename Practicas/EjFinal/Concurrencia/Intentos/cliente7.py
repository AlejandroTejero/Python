import socket
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5557))
print(f"Cliente corriendo en direccion: {client_socket.getsockname()}")

try:
    while True:
        cancion = input('Introduzca cancion: ')
        artista = input('Introduzca artista: ')
        if artista == 'exit':
            print('Cliente cerrado por exit')
            break
        dicc = {'Cancion': cancion, 'Artista': artista}
        client_socket.sendall(pickle.dumps(dicc))
        lista = pickle.loads(client_socket.recv(1024))
        print(f"La lista obtenida es: {lista}")
except KeyboardInterrupt:
    pass

client_socket.close()

