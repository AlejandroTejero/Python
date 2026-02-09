import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5555))
server_socket.listen(1)

print(f"Server running on {server_socket.getsockname()}")

info = []
try:
    while True:
        print("Listenning...")
        client_socket, client_address = server_socket.accept()
        if client_socket:
            print(f"New client connected: {client_address}")
            while True:
                msg = client_socket.recv(1024)
                if not msg:
                    print(f"Client {client_address} closed connection")
                    client_socket.close()
                    break
                data = pickle.loads(msg, encoding='utf-8')
                print(f"Data received: {data}")
                info.append(data)
                client_socket.sendall(pickle.dumps(info))
except KeyboardInterrupt:
    server_socket.close()
    print("Server closed")
