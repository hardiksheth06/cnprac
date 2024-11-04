import socket
import time

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 9999

# Bind the socket to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

while True:
    # Establish a connection
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))

    # Get the current time
    currentTime = time.ctime(time.time()) + "\r\n"

    # Send the current time to the client
    clientsocket.send(currentTime.encode('ascii'))

    # Close the client connection
    clientsocket.close()
