import socket

host = '127.0.0.1'
port = 5000

obj = socket.socket()
obj.connect((host, port))
print("Conectado al bus")

while True:
    mens = input("Mensaje desde Cliente a Servidor >> ")
    obj.sendto(mens.encode('utf-8'), (host, port))
obj.close()
print("Conexión cerrada")