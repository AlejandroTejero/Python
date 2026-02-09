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
            existe = True
            client_socket.sendall(pickle.dumps(existe))
            lineas = fichero.read().splitlines()
            total = len(lineas)
            lineas_enviadas = 0
            for linea in lineas:
                palabra = linea.split(",")
                dicc = {'Titulo': palabra[0],'Temporada': palabra[1],
                        'Episodio': palabra[2],
                        'Ultimo': lineas_enviadas == total - 1}
                client_socket.sendall(pickle.dumps(dicc))
                lineas_enviadas += 1
                if lineas_enviadas != total:
                    next_line = pickle.loads(client_socket.recv(4))
                    if not next_line:
                        break
            if lineas_enviadas == total:
                print('Fichero enviado por completo')
    except FileNotFoundError:
        print(f"Fichero {nombre_fichero} no encontrado")
        client_socket.sendall(pickle.dumps(existe))

    server_socket.close()
    print('Servidor cerrado')



