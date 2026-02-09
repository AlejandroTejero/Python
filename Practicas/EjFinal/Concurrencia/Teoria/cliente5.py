import sys
import socket

'''if len(sys.argv) != 3:
    print("Usage: python3 client.py <server_ip> <server_port>")
    sys.exit(1)'''

server_ip = sys.argv[1]
server_port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("Connected to server")

try:
    while True:
        msg = input("Please, enter a message: ")
        if msg == "bye bye":
            break
        client_socket.send(msg.encode())
        response = client_socket.recv(1024)
        str_response = response.decode()
        print(f"Server response: {str_response}")
except KeyboardInterrupt:
    pass

client_socket.close()
print()
print("Connection closed")
