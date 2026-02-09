import sys
import pickle
import socket

port = 2003
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),port))
print(f"Connected running in {client_socket.getsockname()}")

file_name = input('Introduzca el nombre del fichero')
client_socket.sendall(file_name.encode())
file_exist = pickle.loads(client_socket.recv(4))
print(f"Fichero existe: {file_exist}")
if file_exist:
    next_line = True
    while next_line:
        line = client_socket.recv(1024).decode()
        if line == 'EOF':
            print('Se ha alcanzado fin de fichero')
            break
        print(line)
        print()
        avanzar = input()
        if avanzar == 'q':
            print('Transmision acabada')
            next_line = False
        client_socket.sendall(pickle.dumps(next_line))

else:
    print('Fichero no existente')


client_socket.close()
print('Cliente cerrado')


