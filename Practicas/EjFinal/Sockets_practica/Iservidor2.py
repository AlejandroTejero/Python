import socket
import pickle

HOST = socket.gethostname()
PORT = 2001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Corriendo en {server_socket.getsockname()}")

while True:
    client_socket,client_address = server_socket.accept()
    print(f"Conectado al cliente {client_address}")
    file_name = client_socket.recv(1024)
    print(f'Nombre del archivo buscado: {file_name}')

    file_exist = False
    try:
        with open(file_name) as file:
            file_exist = True
            lines = file.read().splitlines()
            client_socket.sendall(pickle.dumps(file_exist))
            print('Enviando lineas...')
            lines_read = len(lines)
            total = 0
            for line in lines:
                linea = line.split(",")
                frase = {'peli': linea[0],
                         'temp': linea[1],
                         'cap': linea[2]}
                client_socket.sendall(pickle.dumps(frase))
                total += 1
                next_line = pickle.loads(client_socket.recv(4))
                if not next_line:
                    break
    except FileNotFoundError:
        print(f"Archivo {file_name} no encontrado")

    client_socket.close()
    print('Conexion finalizada')