import socket

# Fungsi untuk mengecek apakah sebuah bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

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
    
    # Ubah pesan menjadi bilangan integer
    number = int(data.decode())

    # Cek apakah bilangan prima
    if is_prime(number):
        response = f'{number} adalah bilangan prima.'
    else:
        response = f'{number} bukan bilangan prima.'
    
    # Kirim balasan ke klien
    server_socket.sendto(response.encode(), client_address)
