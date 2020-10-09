from socket import create_connection

# Conectar al servidor.
with create_connection(("127.0.0.1", 5000)) as conn:
    print("Conectado al bus.")
    # Enviar datos.
    conn.sendall(b"Hola profe!")

print("Conexión cerrada.")