import sys
import socket
import pickle

SERVER_HOST = sys.argv[1]
SERVER_PORT = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f"FTP client running on {client_socket.getsockname()}")

file_name = input("File's name: ")
client_socket.sendall(file_name.encode('utf-8')) #codigo en el q se codifica
file_exists = pickle.loads(client_socket.recv(4)) #recibe 4 bytes pq es un boolean = 4 bytes y los decodifica con loads
if file_exists: # si el booleano es true
    next_line = True
    while next_line:
        line = client_socket.recv(1024).decode('utf-8') #recibes 1024 bytes y lo decoficas a utf8
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
