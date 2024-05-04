import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 4096
client_socket = None

def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to server")

def list_files():
    client_socket.send(b"ls")
    files = client_socket.recv(BUFFER_SIZE).decode()
    print("Files and folders in current directory:")
    print(files)

def remove_file(file_name):
    client_socket.send(("rm " + file_name).encode())
    print(client_socket.recv(BUFFER_SIZE).decode())

def download_file(file_name):
    client_socket.send(("download " + file_name).encode())
    file_length = int.from_bytes(client_socket.recv(4), byteorder='big')
    received_bytes = 0
    download_folder = "download"  # Specify the download folder
    file_path = os.path.join(download_folder, file_name)
    with open(file_path, 'wb') as file:
        while received_bytes < file_length:
            data = client_socket.recv(min(BUFFER_SIZE, file_length - received_bytes))
            if not data:
                break
            file.write(data)
            received_bytes += len(data)
    print("Downloaded", file_name, "to", download_folder)

def upload_file(file_name):
    if os.path.exists(file_name):
        client_socket.send(("upload " + file_name).encode())
        with open(file_name, 'rb') as file:
            client_socket.sendfile(file)
        print("Uploaded", file_name)
    else:
        print("File not found.")

def file_size(file_name):
    client_socket.send(("size " + file_name).encode())
    size = client_socket.recv(BUFFER_SIZE).decode()
    if os.path.exists(file_name):
        print("File size of", file_name, "is", size, "MB")
    else:
        print("File not found.")

def disconnect():
    client_socket.send(b"byebye")
    client_socket.close()
    print("Disconnected from server")

def main():
    print("-----LIST OF COMMANDS -----")
    print("connme              : Connect to server (do this first !)")
    print("ls                  : List files")
    print("rm <file_name>      : Delete file")
    print("download <file_name>: Download file")
    print("upload <file_name>  : Upload file")
    print("size <file_name>    : Get file size")
    print("byebye              : Exit program\n")   

    while True:
        command = input("Enter command: ").strip()
        if command == "connme":
            connect_to_server()
            break
        else:
            print("Please type 'connme' to connect to the server first.")

    while True:
        command = input("\nEnter command: ").strip()
        if command == "ls":
            list_files()
        elif command.startswith("rm"):
            _, file_name = command.split(maxsplit=1)
            remove_file(file_name)
        elif command.startswith("download"):
            _, file_name = command.split(maxsplit=1)
            download_file(file_name)
        elif command.startswith("upload"):
            _, file_name = command.split(maxsplit=1)
            upload_file(file_name)
        elif command.startswith("size"):
            _, file_name = command.split(maxsplit=1)
            file_size(file_name)
        elif command == "byebye":
            disconnect()
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
