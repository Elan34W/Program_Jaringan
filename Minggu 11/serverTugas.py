import socket

# Inisialisasi socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port tertentu
server_address = ('localhost', 5000)
sock.bind(server_address)

# Menunggu koneksi masuk
sock.listen(1)
print('Menunggu koneksi dari klien...')

while True:
    # Menerima koneksi dari klien
    client_socket, client_address = sock.accept()
    print('Terhubung dengan klien:', client_address)

    while True:
        # Menerima pesan dari klien
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print('Pesan diterima dari klien:', data)

        # Memisahkan operator dan operand
        try:
            operand1, operator, operand2 = data.split()
            operand1 = int(operand1)
            operand2 = int(operand2)

            # Melakukan perhitungan matematika
            result = None
            if operator == '+':
                result = operand1 + operand2
            elif operator == '-':
                result = operand1 - operand2
            elif operator == '*':
                result = operand1 * operand2
            elif operator == '/':
                result = operand1 / operand2

            # Mengirim pesan balasan berisi hasil perhitungan ke klien
            response = str(result)
        except Exception as e:
            response = f"Error: {e}"

        client_socket.send(response.encode())

    # Menutup koneksi dengan klien
    client_socket.close()
