import  pickle
import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5555))
print(f"Cliente {client_socket.getsockname()} corriendo")

nombre_fichero = input('Introduzca nombre fichero: ')
client_socket.sendall(nombre_fichero.encode())
existe = pickle.loads(client_socket.recv(4))
if existe:
    print(f"Fichero {nombre_fichero} encontrado")
    siguiente_linea = True
    while siguiente_linea:
        diccionario = pickle.loads(client_socket.recv(1024))
        print(diccionario)
        if diccionario['Ultimo']:
            siguiente_linea = False
            print('Has llegado al fin del fichero')

        user_input = input('Introduzca caracter: ')
        if user_input == 'q':
            print('Fin por "q"')
            siguiente_linea = False

        client_socket.sendall(pickle.dumps(siguiente_linea))
else:
    print(f"El fichero {nombre_fichero} no existe")

client_socket.close()
print('Cliente cerrado')