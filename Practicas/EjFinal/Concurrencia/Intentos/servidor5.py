import socket
import pickle
import threading

lita = []
cerrojo = threading.Lock()
def handle_client(client_socket,client_address):
    global lista,cerrojo

    print(f"Cliente con direccion ({client_address}) conectado")
    while True:
        frase = client_socket.recv(1024)
        if not frase:
            print('No datos, cliente cerrado')
            client_socket.close()
            break
        str_frase = pickle.loads(frase)
        print(f"Frase recibida de {client_address}: {str_frase}")
        cerrojo.acquire()
        '''lista.append(str_frase)
        client_socket.sendall(pickle.dumps(lista).upper())
        cerrojo.release()'''
        client_socket.sendall(pickle.dumps(str_frase).upper())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5556))
server_socket.listen()
print(f"Servidor corriendo en {server_socket.getsockname()}")

try:
    while True:
        client_socket,client_address = server_socket.accept()
        t = threading.Thread(target=handle_client,args=[client_socket,client_address])
        t.start()
except KeyboardInterrupt:
    server_socket.close()
    print('Servidor cerrado con Ctrl+C')