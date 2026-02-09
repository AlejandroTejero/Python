import sys
import socket
import pickle

SERVER_HOST = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"FTP client running on {client_socket.getsockname()}")

file_name = input("File's name: ")
client_socket.sendall(file_name.encode('utf-8'))

file_exists = pickle.loads(client_socket.recv(4))
if file_exists:
    next_line = True
    while next_line:
        line = client_socket.recv(1024).decode('utf-8')
        if line == "EOF":
            print("Transfer complete")
            break
        print(line, end="")

        user_input = input()
        if user_input == "q":
            next_line = False
        client_socket.sendall(pickle.dumps(next_line))
else:
    print(f"File '{file_name}' doesn't exist")

client_socket.close()
print("Bye!")
