import socket

# Server setup
localIP = "127.0.0.1"        # Local IP address
localPort = 20001            # Port to listen on
bufferSize = 1024            # Buffer size for receiving data

# Message to send to clients
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket (UDP socket)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind the socket to the IP and port
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while True:
    # Receive data from client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]    # Message content
    address = bytesAddressPair[1]    # Client address (IP, port)

    # Display client message and address
    clientMsg = "Message from Client: {}".format(message)
    clientIP = "Client IP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)

    # Send a reply back to the client
    UDPServerSocket.sendto(bytesToSend, address)
