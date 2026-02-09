import pickle
import socket

port = 2005
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),port))
print('Cliente running...')

file_name = input('File name: ')
client_socket.sendall(file_name.encode())
file_exist = pickle.loads(client_socket.recv(4))
print(f"FILE EXIST {file_exist}")
if file_exist:
    print('HOlA')
    next_line = True
    while next_line:
        print('Recibiendo lineas...')
        serie = pickle.loads(client_socket.recv(1024))
        print(serie)
        if serie['Name'] == 'Last':
            print('End Conexion')
            break

        user_input = input()
        if user_input == 'q':
            print('End conexion')
            next_line = False
        #pickle.dumps(client_socket.sendall(next_line))
        client_socket.sendall(pickle.dumps(next_line))
else:
    print(f"File {file_name} doesnt exist")
client_socket.close()
print('CONEXION FINALIZADA')