'''import socket
import sys
import pickle

puerto = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),puerto))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Cliente con direccion {client_address} conectado")
    nombre_fichero = client_socket.recv(1024).decode('utf-8')
    existe = False
    print(f"Buscando fichero ({nombre_fichero})")
    try:
        with open(nombre_fichero,'r') as file:
            print('Fichero encontrado')
            existe = True
            client_socket.sendall(pickle.dumps(existe))

            print('Leyendo fichero')

            lineas = file.read().splitlines()
            total = len(lineas)
            lineas_enviadas = 0
            for linea in lineas:
                print(f"Linea leida: {linea}")
                if linea != "":
                    client_socket.sendall(linea.encode('utf-8'))
                    if lineas_enviadas != total:
                        siguiente_linea = pickle.loads(client_socket.recv(4))
                        if not siguiente_linea:
                            break
                lineas_enviadas += 1
            if lineas_enviadas == total:
                client_socket.sendall('EOF'.encode())
    except FileNotFoundError:
        client_socket.sendall(pickle.dumps(existe))
        print('El fichero no existe')
        client_socket.sendall(pickle.dumps(existe))'''

import socket
import sys
import pickle

puerto = int(sys.argv[1])

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),puerto))
server_socket.listen()
print(f"Cliente corriendo en {server_socket.getsockname()}")

while True:
    client_socket,client_address = server_socket.accept()
    print(f"Cliente con direccion ({client_address}) conectado")
    nombre_fichero = client_socket.recv(1024).decode()
    print(f"El nombre del fichero que buscamos es: {nombre_fichero}")
    existe = False
    try:
        with open(nombre_fichero,'r') as fichero:
            existe = True
            client_socket.sendall(pickle.dumps(existe))

            lineas = fichero.read().splitlines()
            for linea in lineas:
                print(f"Linea leida = {linea}")
                client_socket.sendall(linea.encode())
                letra = client_socket.recv(1024).decode()
    except FileNotFoundError:
        client_socket.sendall(pickle.dumps(existe))




