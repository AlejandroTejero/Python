import socket
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5555))
print(f"Connected to server {client_socket.getsockname()}")

dicc = {}

try:
    while True:
        song = input('Cancion: ')
        artist = input('Artista: ')
        if artist.lower() == 'exit':
            print('Conexion finalizada')
            break
        #dicc = {'song': song, 'artist': artist}
        dicc['song'] = song
        dicc['artist'] = artist
        data = pickle.dumps(dicc)
        client_socket.sendall(data)
        data_response = client_socket.recv(1024)
        str_data_response = pickle.loads(data_response)
        print(str_data_response)
except KeyboardInterrupt:
    pass

client_socket.close()
print('Conexion finalizada')


