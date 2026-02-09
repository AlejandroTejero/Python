'''import socket
import sys
import pickle

ip = sys.argv[1]
puerto = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip,puerto))
print(f"Cliente corriendo en {client_socket.getsockname()}")

nombre_fichero = input('Introduzca nombre del fichero: ')
client_socket.sendall(nombre_fichero.encode('utf-8'))
existe = pickle.loads(client_socket.recv(4))
print(existe)
if existe:
    siguiente_linea = True
    while siguiente_linea:
        linea = client_socket.recv(1024).decode('utf-8')
        print(f"La linea es: {linea}")
        if linea == 'EOF':
            print('Se ha acabado la lectura del fichero')
            break

        user_input = input('Introduzca una letra: ')
        if user_input == 'q':
            siguiente_linea = False
        client_socket.sendall(pickle.dumps(siguiente_linea))
else:
    print('No se ha encontrado el fichero')

client_socket.close()
print('Cliente cerrado')'''

import socket
import sys
import pickle

ip = sys.argv[1]
puerto = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip,puerto))
print(f"Cliente corriendo en {client_socket.getsockname()}")

print('Introduzca el nombre del fichero:')
nombre_fichero = input()
client_socket.sendall(nombre_fichero.encode())
existe = pickle.loads(client_socket.recv(4))
print(f"El fichero buscado existe?: {existe}")
if existe:
    siguiente_linea = True
    while siguiente_linea:
        linea = client_socket.recv(1024).decode()
        print(f"La linea es: {linea}")
        if linea == 'EOF':
            break

        user_input = input('Introduzca letra: ')
        if user_input == 'q':
            siguiente_linea = False
            client_socket.sendall(user_input.encode())

        client_socket.sendall(user_input.encode())
else:
    print(f"El fichero con {nombre_fichero} no existe")

