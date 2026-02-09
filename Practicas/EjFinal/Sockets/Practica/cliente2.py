import  pickle
import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5555))
print(f"Cliente {client_socket.getsockname()} corriendo")

nombre_fichero = input('Introduzca el nombre del fichero: ')
client_socket.sendall(nombre_fichero.encode())
print(f"Mensaje enviado")
existe = pickle.loads(client_socket.recv(4))
if existe:
    next_line = True
    while next_line:
        print(f"El fichero {nombre_fichero} existe")
        dicc = pickle.loads(client_socket.recv(1024))
        print(dicc)
        if dicc['Ultimo']:
            print('Fichero leido por completo')
            break

        letra = input('Introduzca letra: ')
        if letra == 'q':
            next_line = False
            print('Cliente cerrado por q')
        client_socket.sendall(pickle.dumps(next_line))
else:
    print(f"El fichero {nombre_fichero} no existe")

client_socket.close()
print('Cliente cerrado')