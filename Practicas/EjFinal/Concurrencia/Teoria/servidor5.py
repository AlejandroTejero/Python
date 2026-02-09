import sys
import socket
import threading


def client_handler(client_socket, client_address):
    print(f"New client connected: {client_address}")
    if client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Client {client_address} closed connection")
                client_socket.close()
                break
            msg = data.decode()
            print(f"Message received: {msg}")
            client_socket.sendall(msg.encode().upper())


'''if len(sys.argv) != 2:
    print("Usage: python3 server.py <port>")
    sys.exit(1)'''

port = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), port))
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
