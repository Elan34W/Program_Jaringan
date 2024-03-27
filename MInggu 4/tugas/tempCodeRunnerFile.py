import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
print(f"Starting server on {server_address[0]} port {server_address[1]}")
server_socket.bind(server_address)
server_socket.listen(1)
while True:
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")
        data = connection.recv(1024)
        if data:
            jumlah_karakter = len(data.decode('utf-8'))
            connection.sendall(str(jumlah_karakter).encode('utf-8'))
        else:
            print("Tidak menerima data apapun.")
    finally:
        connection.close()

