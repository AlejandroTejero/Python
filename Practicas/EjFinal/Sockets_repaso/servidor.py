import socket

WELCOME_MESSAGE = "Welcome to the server!"

clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen(2)
print(f"Server running on {server_socket.getsockname()}")


for n in range(1,3):
    client_socket,client_address = server_socket.accept()
    print(f"Conectado a {n}, {client_address}")
    clients.append({'socket': client_socket, 'address': client_address})
    client_socket.sendall(WELCOME_MESSAGE.encode())

noc = 0
for client in clients:
    socket = client['socket']
    ac = clients[(noc +1) % 2]
    ip = ac['address'][0]
    socket.sendall(ip.encode())
