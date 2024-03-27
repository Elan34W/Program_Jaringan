import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
client_socket.connect(server_address)
try:
    message = input("Enter your message: ")
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print(f"Received response: {data.decode('utf-8')}")

finally:
    client_socket.close()

