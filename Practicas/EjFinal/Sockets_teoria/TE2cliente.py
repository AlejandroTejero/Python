import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 5555))
print("Connected to server")

try:
    while True:
        msg = input("Please, enter a message: ")
        if msg == "bye bye":
            break
        client_socket.send(msg.encode())
        response = client_socket.recv(1024)
        str_response = response.decode()
        print(f"Server response: {response.decode()}")
except KeyboardInterrupt:
    pass

client_socket.close()
print()
print("Connection closed")
