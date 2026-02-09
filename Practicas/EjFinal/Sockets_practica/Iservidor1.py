import socket
import pickle

HOST = socket.gethostname()
PORT = 2003

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"FTP server running on {server_socket.getsockname()}")


while True:
    lista_lineas = []
    client_socket,client_address = server_socket.accept()
    if client_socket:
        print(f"Conectado a cliente = {client_address}")
        nombre_fichero = client_socket.recv(1024).decode('utf-8')
        print(f"Nombre del fichero pedido = {nombre_fichero}")
        file_exists = False
        try:
            with open(nombre_fichero) as fichero:
                file_exists = True
                lines = fichero.read().splitlines()
                lista_lineas.append(lines)
                for line in lines:
                    if line != "":
                        client_socket.sendall(pickle.dumps(line))
                        print(f"linea enviada = {line}")
        except:
            print(f"Fichero {nombre_fichero} no existente")

    server_socket.close()
