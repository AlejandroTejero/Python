import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
print(f"Client running on {client_socket.getsockname()}")

welcome_mensagge = client_socket.recv(1024).decode()
print(welcome_mensagge)

another_client_ip = client_socket.recv(1024).decode('utf-8')
print(f"IP from another client {another_client_ip}")

client_socket.close()
print("Client closed")

