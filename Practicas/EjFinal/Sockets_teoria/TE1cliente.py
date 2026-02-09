'Escritura 1.0'
import sys
import socket

ip = sys.argv[1]
puerto = sys.argv[2]
cliente_socket = socket.socket(socket.SOCK_STREAM,socket.AF_INET)
cliente_socket.connect((ip,puerto))
print("Conectado al servidor")

name = input("Porfavor introduzca el nombre")
cliente_socket.send((name.encode()))
print(f"Mensaje: {name}")

cliente_socket.close()
print(f"conexion cerrada")

'Escritura 2.0'
'''import sys
import socket

ip = sys.argv[1]
puerto = sys.argv[2]
cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(ip,puerto)
print(f"Conectado al servidor")

name = input('nombre:')
cliente_socket.send(name.encode())
print('mensaje: ')
cliente_socket.close()
print('conex cerrada')'''

'Escritura 3.0'
'''import sys
import socket

ip = sys.argv[1]
puerto = sys.argv[2]
cliente_socket = socket.socket(socket.AF_INET, socket.AF_INET)
cliente_socket.connect(ip,puerto)
print('conectado')

name = input('name:')
cliente_socket.send(name.encode())
print('enviado')
cliente_socket.close()'''

'Escritura 4.0'
'''import sys
import socket

ip = sys.argv[1]
puerto = sys.argv[2]

cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente_socket.connect(ip,puerto)
print('conectado')

name = input('nombre: ') 
cliente_socket.send(name.encode())
print('enviando...')

cliente_socket.close()
print('conexion cerrada')'''

'Escritura 5.0'
'''import sys
import socket

ip = sys.argv[1]
port = int(sys.argv[2])
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip,port))
print('Conectando...')

name = input('Introduzca su nombre')
client_socket.send(name.encode())
print('Enviando datos...')
client_socket.close()
print('Finalizando conexion...')'''