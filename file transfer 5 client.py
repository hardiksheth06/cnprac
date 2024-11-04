import socket

# Client message setup
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)

# Server address (IP and port)
serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at the client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send message to the server using the created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Receive response from the server
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

# Display the server's response
msg = "Message from Server: {}".format(msgFromServer[0])
print(msg)
