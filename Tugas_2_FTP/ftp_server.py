import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 4096

def list_files():
    files = os.listdir('.')
    return '\n'.join(files)

def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        return f"{file_name} removed successfully."
    else:
        return f"File {file_name} not found."

def download_file(file_name, client_socket):
    if os.path.exists(file_name):
        try:
            with open(file_name, "rb") as f:
                data = f.read()
                file_length = len(data)
                client_socket.sendall(file_length.to_bytes(4, byteorder='big'))
                client_socket.sendall(data)
                return b"Download successful."
        except Exception as e:
            return f"Failed to download file: {str(e)}".encode()
    else:
        return b"File not found."

def upload_file(file_name, data):
    if os.path.exists(file_name):
        return "File already exists on server."
    else:
        with open(file_name, 'wb') as file:
            file.write(data)
        return f"{file_name} uploaded successfully."

def file_size(file_name):
    if os.path.exists(file_name):
        size = os.path.getsize(file_name) / (1024 * 1024)
        return f"{size:f}"
    else:
        return f"File {file_name} not found."

def handle_command(command, client_socket):
    if command == "ls":
        return list_files()
    elif command.startswith("rm"):
        _, file_name = command.split(maxsplit=1)
        return remove_file(file_name)
    elif command.startswith("download"):
        _, file_name = command.split(maxsplit=1)
        return download_file(file_name, client_socket)
    elif command.startswith("upload"):
        _, file_name = command.split(maxsplit=1)
        return "Ready to receive file", file_name
    elif command.startswith("size"):
        _, file_name = command.split(maxsplit=1)
        return file_size(file_name)
    else:
        return "Invalid command"
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)
    print("Server listening...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE).decode()
            if not data:
                break
            if data.startswith("upload"):
                _, file_name = data.split(maxsplit=1)
                client_socket.send(b"ready")
                file_data = client_socket.recv(BUFFER_SIZE)
                result = upload_file(file_name, file_data)
                client_socket.send(result.encode())                     
            else:
                response = handle_command(data, client_socket)
                if isinstance(response, tuple):
                    message, file_name = response
                    client_socket.send(message.encode())
                    file_data = client_socket.recv(BUFFER_SIZE)
                    result = upload_file(file_name, file_data)
                    client_socket.send(result.encode())
                else:
                    client_socket.send(response.encode())
        except Exception as e:
            print("Error:", e)
            client_socket.close()
            break

if __name__ == "__main__":
    main()
