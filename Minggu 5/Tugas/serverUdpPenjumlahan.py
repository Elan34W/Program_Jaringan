import socket

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ikuti alamat dan port yang digunakan oleh server
server_address = ('localhost', 8000)
server_socket.bind(server_address)

print('Menunggu koneksi...')

total_sum = 0  # Inisialisasi total penjumlahan

while True:
    # Terima pesan dari klien
    data, client_address = server_socket.recvfrom(1024)
    print('Menerima pesan dari client', data.decode())
    
    # Ubah pesan menjadi bilangan bulat
    number = int(data.decode())
    
    # Tambahkan bilangan ke total penjumlahan
    total_sum += number
    
    # Kirim total penjumlahan ke klien
    server_socket.sendto(str(total_sum).encode(), client_address)
