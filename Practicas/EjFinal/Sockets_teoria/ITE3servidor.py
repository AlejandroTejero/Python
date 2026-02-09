import pickle
import socket

lista_vacia = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 555))
server_socket.listen(1)
print(f"Server running on {server_socket.getsockname()}")

client_socket,client_address = server_socket.accept()
if client_socket:
    print(f"Conectado a {client_address}")
    while True:
        data = client_socket.recv(1024)
        if not data:
            print('No hay datos')
            break
        str_data = pickle.loads(data)
        print(str_data)
        lista_vacia.append(str_data)
        data_response = pickle.dumps(lista_vacia)
        client_socket.sendall(data_response)

server_socket.close()
print('Conexion servidor finalizada')