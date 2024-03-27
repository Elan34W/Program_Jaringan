import socket

# Fungsi untuk mengecek apakah sebuah string palindrom atau tidak
def is_palindrome(s):
    return s == s[::-1]

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ikuti alamat dan port yang digunakan oleh server
server_address = ('localhost', 8000)
server_socket.bind(server_address)

print('Menunggu koneksi...')

while True:
    # Terima pesan dari klien
    data, client_address = server_socket.recvfrom(1024)
    print('Menerima pesan dari client', data.decode())
    
    # Ubah pesan menjadi string
    message = data.decode()
    
    # Cek apakah pesan merupakan palindrom atau tidak
    if is_palindrome(message):
        response = 'Input adalah palindrom.'
    else:
        response = 'Input bukan palindrom.'
    
    # Kirim balasan ke klien
    server_socket.sendto(response.encode(), client_address)
