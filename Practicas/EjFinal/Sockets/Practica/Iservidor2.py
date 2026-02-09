import  pickle
import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5555))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")


while True:
    client_socket,client_address = server_socket.accept()
    print(f"Cliente con direccion {client_address} conectado")
    nombre_fichero = client_socket.recv(1024).decode()
    existe = False
    try:
        with open(nombre_fichero,'r') as fichero:
            print(f"El fichero {nombre_fichero} existe")
            existe = True
            client_socket.sendall(pickle.dumps(existe))

            lineas = fichero.read().splitlines()
            total = len(lineas)
            lineas_enviadas = 0
            for linea in lineas:
                palabras = linea.split(",")
                diccionario = {'Titulo': palabras[0],'Temporadas': palabras[1],
                               'Episodios': palabras[2],
                               'Ultimo': lineas_enviadas == total - 1}
                client_socket.sendall(pickle.dumps(diccionario))
                lineas_enviadas += 1
                if lineas_enviadas != total:
                    siguiente_linea = pickle.loads(client_socket.recv(4))
                    if not siguiente_linea:
                        break
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no existe")
        client_socket.sendall(pickle.dumps(existe))

    server_socket.close()
    print('Servidor cerrado')
