import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5556))
server_socket.listen(1)

print(f"Servidor corriendo en {server_socket.getsockname()}")
lista = []

try:
    while True:
        client_socket,client_address = server_socket.accept()
        if client_socket:
            while True:
                print(f"Cliente con direccion ({client_address}) conectado")
                dicc = client_socket.recv(1024)
                if not dicc:
                    client_socket.close()
                    break
                str_dicc = pickle.loads(dicc)
                lista.append(str_dicc)
                print(f"Diccionario ({str_dicc}) añadido a la lista")
                client_socket.sendall(pickle.dumps(lista))
except KeyboardInterrupt:
    print('Servidor cerrado por Ctr+C')

server_socket.close()