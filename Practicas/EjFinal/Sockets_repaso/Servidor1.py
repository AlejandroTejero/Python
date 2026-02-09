import socket

HOST = socket.gethostname()
PORT = 12345
NUMBER_OF_CLIENTS = 2
WELCOME_MESSAGE = "Welcome to the server!"

clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(NUMBER_OF_CLIENTS)
print(f"Server running on {server_socket.getsockname()}")

for n in range(1, NUMBER_OF_CLIENTS + 1):
    print(f"Listenning for client {n}")
    client_socket, client_address = server_socket.accept()
    print(f"Client {n} connected: {client_address}")
    clients.append({'socket': client_socket, 'address': client_address})
    client_socket.sendall(WELCOME_MESSAGE.encode('utf-8'))

noc = 0
for client in clients:
    socket = client['socket']
    ac = clients[(noc + 1) % 2]
    ip = ac['address'][0]
    socket.sendall(ip.encode('utf-8'))
    noc += 1

for client in clients:
    socket = client['socket']
    message = socket.recv(1024).decode()
    if not message:
        socket.close()

server_socket.close()
print("Server closed")

