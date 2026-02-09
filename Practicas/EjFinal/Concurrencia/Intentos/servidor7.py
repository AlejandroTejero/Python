import pickle
import socket
import threading

cerrojo = threading.Lock()
lista_privada = []
dicc_privado = {}
def handle_client(client_socket,client_address):
    global cerrojo,lista_privada,dicc_privado

    print(f"Cliente ({client_address}) conectado")
    if client_socket:
        while True:
            dicc = client_socket.recv(1024)
            if not dicc:
                client_socket.close()
                print(f"Cliente ({client_address}) cerrado")
                break
            str_dicc = pickle.loads(dicc)
            print(f"Mensaje recibo = {str_dicc}")

            cerrojo.acquire()
            if client_address in dicc_privado:
                dicc_privado[client_address].append(str_dicc)
            else:
                dicc_privado[client_address] = [str_dicc]
            cerrojo.release()
            client_socket.sendall(pickle.dumps(lista_privada[client_address]))


            '''cerrojo.acquire()
            lista_privada.append(str_dicc)
            cerrojo.release()
            client_socket.sendall(pickle.dumps(lista_privada))'''



server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(),5557))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

try:
    while True:
        client_socket,client_address = server_socket.accept()
        t = threading.Thread(target=handle_client,
                             args=[client_socket,client_address])
        t.start()
except KeyboardInterrupt:
    print('Servidor cerrado con Ctrl+C')

server_socket.close()