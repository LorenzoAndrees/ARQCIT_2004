import socket

host = '127.0.0.1'
port = 5000

obj = socket.socket()
obj.connect((host, port))
print("Conectado al bus")

while True:
    mens = raw_input("Mensaje desde Cliente a Servidor >> ")
    obj.send(mens)
obj.close()
print("Conexión cerrada")