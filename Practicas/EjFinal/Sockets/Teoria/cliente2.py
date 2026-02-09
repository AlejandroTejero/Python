import socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),5555))
print(f"Cliente corriendo en {client_socket.getsockname()}")

try:
    while True:
        mensaje = input('Introduzca el mensaje: ')
        if mensaje == 'bye bye':
            print("Servidor cerrado con bye bye")
            break

        client_socket.sendall(mensaje.encode())
        mensaje_upper = client_socket.recv(1024).decode()
        print(f"Mensaje recibido del servidor: {mensaje_upper}")
except KeyboardInterrupt:
    print("Cliente cerrado con Ctrl + C")
    client_socket.close()