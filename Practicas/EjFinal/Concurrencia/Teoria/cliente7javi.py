import socket
import pickle


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5555))
print("Connected to server")

try:
    while True:
        song = input("Please, enter a song: ")
        artist = input("Please, enter song's artist: ")
        if artist == "exit":
            break
        data = {'song': song, 'artist': artist}
        client_socket.send(pickle.dumps(data))

        response = client_socket.recv(1024)
        data = pickle.loads(response)
        print(f"Server response: {data}")
except KeyboardInterrupt:
    pass

client_socket.close()
print()
print("Connection closed")
