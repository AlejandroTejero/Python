import socket
import threading
import pickle

songs = {}
lock = threading.Lock()


def client_handler(client_socket, client_address):
    global songs, lock

    print(f"New client connected: {client_address}")
    if client_socket:
        while True:
            msg = client_socket.recv(1024)
            if not msg:
                print(f"Client {client_address} closed connection")
                client_socket.close()
                break
            song = pickle.loads(msg, encoding='utf-8')
            print(f"Data received from {client_address}: {song}")
            lock.acquire()
            if client_address in songs:
                songs[client_address].append(song)
            else:
                songs[client_address] = [song]
            client_socket.sendall(pickle.dumps(songs[client_address]))
            lock.release()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5555))
server_socket.listen()

print(f"Server running on {server_socket.getsockname()}")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
        thread.start()
except KeyboardInterrupt:
    server_socket.close()
    print("Server closed")
