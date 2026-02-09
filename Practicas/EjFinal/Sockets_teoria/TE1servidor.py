'Escritura 1.0'
import sys
import socket

puerto = sys.argv[1]
servidor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor_socket.bind((socket.gethostname(),puerto))
servidor_socket.listen()

print(f"Servidor conectado en {servidor_socket.getsockname()}")

cliente_socket,cliente_direccion = servidor_socket.accept()
if cliente_socket:
    print(f"Conectado al cliente {cliente_direccion}")
    datos = cliente_socket.recv(1024)
    str_datos = datos.decode()
    print(f"Mensaje recibido {str_datos}")
    
servidor_socket.close()
print(f"Servidor cerrado")

'Escritura 2.0'
'''import sys
import socket

puerto = sys.argv[1]
servidor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor_socket.bind(socket.gethostname(),puerto)
servidor_socket.listen()
print('Escuchando...')

cliente_socket,cliente_direccion = servidor_socket.accept()
if cliente_socket:
    print(f"conectado al cliente {cliente_direccion}")
    datos = cliente_socket.recv(1024)
    str_datos = datos.decode()
    print('mensaje recibido')

servidor_socket.close()
print('Conexion cerrada')'''

'Escritura 3.0'
'''import sys
import socket

puerto = sys.argv[1]
servidor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servidor_socket.bind(socket.gethostname(),puerto)
servidor_socket.listen()
print('Escuchando...')

cliente_socket,cliente_direccion = servidor_socket.accept()
if cliente_socket:
    print(f"Conectado a {cliente_direccion}")
    datos = cliente_socket.recv(1024)
    str_datos = datos.decode()
    print(f"mensaje recibido {str_datos}")

servidor_socket.close()
print('Conexion cerrada')'''

'Escritura 4.0'
'''import sys
import socket

port = int(sys.argv[1])
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),port))
server_socket.listen()
print(f"Escuchando en {server_socket.getsockname()},{port}")

client_socket,client_adress = server_socket.accept()
if client_socket:
    print(f"cliente aceptado con direccion {client_adress}")
    data = client_socket.recv(1024)
    str_data = data.decode()
    print(f"Datos recibidos {str_data}")
server_socket.close()
print('Conexion finalizada')'''