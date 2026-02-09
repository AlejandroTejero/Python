import pickle
import socket

port = 2005
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),port))
server_socket.listen()
print(f"Server running on {server_socket.getsockname()}")

while True:
    client_socket,client_address = server_socket.accept()
    print(f"Client {client_address} connected")
    file_name = client_socket.recv(1024).decode()
    print(f"Name of file: {file_name}")

    file_exist = False
    try:
        with open(file_name) as file:
            file_exist = True
            client_socket.sendall(pickle.dumps(file_exist))
            print(f"File {file_name} exist")


            lines = file.read().splitlines()
            for line in lines:
                frase = line.split(",")
                serie = {'Name': frase[0],
                         'Temp': frase[1],
                         'Cap':frase[2]}
                client_socket.sendall(pickle.dumps(serie))
                next_line = pickle.loads(client_socket.recv(4))
                if not next_line:
                    break
    except FileNotFoundError:
        print(f"File {file_name} not found")

    server_socket.close()
    print('CONEXION FINALIZADA')