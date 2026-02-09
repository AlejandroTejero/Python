import socket

port = 5555
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),port))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")


client_socket,client_address = server_socket.accept()
if client_socket:
    print(f"Conectado con cliente = {client_address}")
    while True:
        data = client_socket.recv(1024)
        if data == None:
            print('Conexion cerrada')
            break
        str_data = data.decode()
        print(f"DATOS RECIBIDOS = {str_data}")
        client_socket.sendall(str_data.encode().upper())

server_socket.close()
print('Servidor finalizado')