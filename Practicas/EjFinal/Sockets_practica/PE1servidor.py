import socket
import pickle

HOST = socket.gethostname()
PORT = 2000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"FTP server running on {server_socket.getsockname()}")

while True:
    print("Listenning...")
    client_socket, client_address = server_socket.accept()
    print(f"New client connected: {client_address}")
    file_name = client_socket.recv(1024).decode('utf-8')
    #file_name = client_socket.recv(1024)
    #str_file_name = file_name.decode()

    file_exists = False
    try:
        with open(file_name) as file:
            file_exists = True
            client_socket.sendall(pickle.dumps(file_exists))

            print(f"Sending file '{file_name}'...")

            lines = file.read().splitlines()
            total = len(lines)
            lines_sent = 0
            for line in lines:
                print(f"Line: |{line}|")
                if line != "":
                    client_socket.sendall(line.encode('utf-8'))
                    if lines_sent != total:
                        next_line = pickle.loads(client_socket.recv(4))
                        if not next_line:
                            break
                lines_sent += 1
                print(f"Lines ({lines_sent}/{total})")
            if lines_sent == total:
                client_socket.sendall("EOF".encode('utf-8'))
                print(f"File '{file_name}' sent")
    except FileNotFoundError:
        print(f"File '{file_name}' doesn't exist")

client_socket.close()
print('Finalizado')
