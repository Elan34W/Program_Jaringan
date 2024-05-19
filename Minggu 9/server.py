import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hellp UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Membuat koneksi socket dengan UDP
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Binding IP dan Port
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen Program    
while(True):
    byteAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = byteAddressPair[0]
    address = byteAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    ClientIP = "Client IP Address:{}".format(address)
    