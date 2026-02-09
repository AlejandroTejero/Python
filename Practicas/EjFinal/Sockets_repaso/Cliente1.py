import sys
import socket

SERVER_HOST = sys.argv[1]
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"Client running on {client_socket.getsockname()}")

welcome_message = client_socket.recv(1024).decode('utf-8')
print(welcome_message)

another_client_ip = client_socket.recv(1024).decode('utf-8')
print(f"IP from another client {another_client_ip}")

client_socket.close()
print("Client closed")
