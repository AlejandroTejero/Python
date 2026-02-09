import socket
import pickle

HOST = socket.gethostname()
PORT = 2003

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"FTP server running on {server_socket.getsockname()}")

while True:
    print("Listenning...")
    client_socket, client_address = server_socket.accept()
    print(f"New client connected: {client_address}")
    file_name = client_socket.recv(1024).decode()

    file_exist = False
    try:
        with open(file_name) as file:
            file_exist = True
            client_socket.sendall(pickle.dumps(file_exist))
            print(f"Enviando existencia del fichero")

            lines = file.read().splitlines()
            total = len(lines)
            lines_sent = 0
            for line in lines:
                print(f"La linea leida es : {line}")
                slices = line.split(",")
                serie = {'serie': slices[0],
                         'temporada': slices[1],
                         'capitulo': slices[2],
                         'last': lines_sent == total - 1}
                client_socket.sendall(pickle.dumps(serie))
                lines_sent += 1
                print(f"Lines ({lines_sent}/{total})")
                if lines_sent != total:
                    next_line = pickle.loads(client_socket.recv(4))
                    if not next_line:
                        break
            if lines_sent == total:
                print(f"File '{file_name}' sent")
    except FileNotFoundError:
        client_socket.sendall(pickle.dumps(file_exist))
        print(f"{file_name} no existe")

    client_socket.close()
