import socket
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5555))
print("Connected to server")

try:
    while True:
        song = input('Song: ')
        artist = input('Artist: ')
        if artist == 'exit':
            print('Conexion cerrada')
            break
        data = {'song': song, 'artist': artist}
        client_socket.sendall(pickle.dumps(data))

        respuesta = client_socket.recv(1024)
        str_respuesta = pickle.loads(respuesta)
        print(f"Respuesta servidor: {str_respuesta}")
except KeyboardInterrupt:
    pass

client_socket.close()
print('Conexion cerrada')

'''import socket
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5555))
print(f"Conectando con direccion {client_socket.getsockname()}")

try:
    while True:
        song = input('Introduzca cancion')
        artist = input('Introduzca artista')
        if artist.lower() == 'exit':
            print('Conexion terminada')
            break
        data = {'artista': artist,'cancion': song}
        print(f"datos: {data}")
        client_socket.sendall(pickle.dumps(data))
        data_vuelta = client_socket.recv(1024)
        str_data_vuelta = pickle.loads(data_vuelta)
        print(f"datos de vuelta: {str_data_vuelta}")
except InterruptedError:
    print('Conexion cerrada')

client_socket.close()
print('CONEXION FINALIZADA')'''