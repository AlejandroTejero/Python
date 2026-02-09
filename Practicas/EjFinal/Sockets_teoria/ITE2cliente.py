import sys
import socket

port = 5555
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),port))
print(f"Cliente conectado en {client_socket.getsockname()}")

try:
    while True:
        msg = input('Introduzca mensaje: ')
        if msg == 'bye bye':
            print('Cliente cerrado por bye bye')
            break
        data = msg.encode()
        client_socket.send(data)
        data_response = client_socket.recv(1024)
        srt_data_response = data_response.decode()
        print(srt_data_response)
except KeyboardInterrupt:
    pass

client_socket.close()
print('Conexion cerrada con Ctrl+C')
