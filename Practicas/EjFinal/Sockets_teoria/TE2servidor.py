import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5555))
server_socket.listen(1)

print(f"Server running on {server_socket.getsockname()}")

client_socket, client_address = server_socket.accept()
if client_socket:
    print(f"New client connected: {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print(f"Client {client_address} closed connection")
            break
        str_data = data.decode()
        print(f"Data received: {str_data}")
        client_socket.sendall(str_data.encode().upper())

server_socket.close()
print("Server closed")