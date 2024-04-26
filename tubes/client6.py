import socket
import time
import threading

# Daftar kata warna dalam bahasa Inggris dan terjemahannya dalam bahasa Indonesia
colors = {
    "red": "merah",
    "green": "hijau",
    "blue": "biru",
    "yellow": "kuning",
    "orange": "jingga",
    "purple": "ungu",
    "pink": "merah muda",
    "brown": "coklat", 
    "white": "putih", 
    "black": "hitam"
}

# Membuat UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket ke alamat dan port
client_address = ('localhost', 8006)
client_socket.bind(client_address)

while True:
    try:
        def input_with_timeout(prompt ,timeout):
            print(prompt)
            response = [None]  # Response will be stored here
            def input_thread():
                try:
                    response[0] = input()
                except Exception as e:
                    print(e)

            thread = threading.Thread(target=input_thread)
            thread.start()
            thread.join(timeout)

            if thread.is_alive():
                print(f"Anda tidak menjawab selama {timeout} detik")
                print("none")
                print("Lanjut ?\n")
                thread.join()
                return None
            else:
                return response[0]

        # Mengirim pesan "connect" ke server
        client_socket.sendto(b'connect', ('localhost', 8000))

        # Menerima pesan dari server
        message, _ = client_socket.recvfrom(1024)
        message = message.decode()

        # Memisahkan kata warna dalam bahasa Inggris dari pesan
        _, random_color_en = message.split(": ")
        print("Kata warna dalam bahasa Inggris yang diterima:", random_color_en)

        # Meminta pengguna untuk memasukkan kata warna dalam bahasa Indonesia
        user_color_id = input_with_timeout("Masukkan kata warna dalam bahasa Indonesia: ",5)

        # Mendapatkan kata warna dalam bahasa Inggris yang sesuai
        correct_color_en = colors.get(random_color_en, "tidak ada")
        
        # Memberikan nilai feedback
        if correct_color_en == user_color_id:
            print("Feedback: 100 (Benar)\n")
        else:
            print("Feedback: 0 (Salah)\n")

    except KeyboardInterrupt:
        print("\nMenutup klien.")
        break

    # Menunggu 5 detik sebelum menerima pesan berikutnya dari server
    time.sleep(5)

# Menutup soket
client_socket.close()
