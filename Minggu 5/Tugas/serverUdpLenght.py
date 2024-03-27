import socket

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ikuti alamat dan port yang digunakan oleh server
server_address = ('localhost', 8000)
server_socket.bind(server_address)

print('Menunggu koneksi...')

while True:
    # Terima pesan dari klien
    data, client_address = server_socket.recvfrom(1024)
    print('Menerima pesan dari client:', data.decode())
    
    # Hitung jumlah karakter dalam pesan
    message_length = len(data.decode())

    # Kirim balasan ke klien
    response = f'Jumlah karakter: {message_length}'
    server_socket.sendto(response.encode(), client_address)
