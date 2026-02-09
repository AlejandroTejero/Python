import pickle
import socket

port = 2003
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),port))
print(f"Connected running in {client_socket.getsockname()}")

file_name = input('File Name: ')
client_socket.sendall(file_name.encode())
file_exist = pickle.loads(client_socket.recv(4))
if file_exist:
    next_line = True
    while next_line:
        serie = pickle.loads(client_socket.recv(1024))
        print(serie)
        if serie['serie'] == 'last':
            print('Se acabo')
            break

        user_input = input()
        if user_input == 'q':
            next_line = False
        client_socket.sendall(pickle.dumps(next_line))
else:
    print('No existe')

client_socket.close()
print('Bye')