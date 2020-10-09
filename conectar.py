from socket import create_connection

# Conectar al servidor.
with create_connection(("localhost", 6190)) as conn:
    print("Conectado al bus.")
    # Enviar datos.
    conn.sendall(b"Hola profe!")

print("Conexión cerrada.")