import pickle
import socket

port = 2001
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),port))
print('Cliente conectado')

file_name = input('Introduzca nombre fichero: ')
client_socket.sendall(file_name.encode())
file_exist = client_socket.recv(4)
if file_exist:
    next_line = True
    while next_line:
        print('Recibiendo lineas...')
        frase = pickle.loads(client_socket.recv(1024))
        print(frase)
        if frase['peli'] == 'Ultimo':
            print('Conexion cerrada')
            break

        user_input = input()
        if user_input == 'q':
            print('Conexion cerrada')
            next_line = False
        client_socket.sendall(pickle.dumps(next_line))

    client_socket.close()
    print('Conexion cerrada')