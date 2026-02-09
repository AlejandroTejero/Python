import socket
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5555))
print(f"Cliente corriendo en {client_socket.getsockname()}")

try:
    while True:
        cancion = input('Introduzcala cancion: ')
        artista = input('Introduzca el artista: ')
        if artista == 'exist':
            break
        dicc = {'Nombre': cancion, 'Artista': artista}
        client_socket.sendall(pickle.dumps(dicc))
        lista = pickle.loads(client_socket.recv(1024))
        print("La lista de los diccionarios es: ")
        print(lista)
except KeyboardInterrupt:
    print("Cliente cerrad con Ctrl + C")

client_socket.close()