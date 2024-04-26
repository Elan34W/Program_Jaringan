import socket
import random
import time
import threading

# Daftar kata warna dalam bahasa Inggris dan terjemahannya dalam bahasa Indonesia
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'white', 'black']

# Membuat UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket ke alamat dan port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

print("UDP server berjalan di {}:{}".format(*server_address))

def handle_client(client_address):
    while True:
        try:
            # Memilih kata warna acak dalam bahasa Inggris
            random_color_en = random.choice(colors)

            # Mengirimkan kata warna acak kepada klien yang terhubung
            message = "Kata warna dalam bahasa Inggris: {}".format(random_color_en)
            server_socket.sendto(message.encode(), client_address)

            print("Kata warna dalam bahasa Inggris yang dikirim kepada {}:{}".format(*client_address), random_color_en)
            
            # Menunggu 10 detik sebelum mengirim kata warna baru
            time.sleep(10)

        except Exception as e:
            print("Error:", e)
            break

# Fungsi untuk menerima koneksi dari klien
def accept_connections():
    while True:
        try:
            # Menerima koneksi dari klien
            data, client_address = server_socket.recvfrom(1024)

            # Tambahkan alamat klien ke set klien yang terhubung
            connected_clients.add(client_address)

            # Tangani klien dalam thread terpisah
            client_thread = threading.Thread(target=handle_client, args=(client_address,))
            client_thread.start()

        except Exception as e:
            print("Error:", e)
            break

# Set klien yang terhubung
connected_clients = set()

# Mulai menerima koneksi dari klien dalam thread terpisah
connection_thread = threading.Thread(target=accept_connections)
connection_thread.start()

# Tunggu hingga semua thread selesai
connection_thread.join()

# Tutup soket
server_socket.close()
