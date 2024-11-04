import socket

# Client configuration
host = "127.0.0.1"  # The server's IP address
port = 12000        # The port used by the server
buffer_size = 1024
file_name = 'MyFile.txt'  # The file to be sent

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the file in read mode
f = open("MyFile.txt", "r")
data = f.read(buffer_size)

# Send the file data to the server
while data:
    print(data)  # Display the data being sent

    # Send data to the server
    if sock.sendto(str.encode(data), (host, port)):
        # Read the next chunk of data
        data = f.read(buffer_size)

# Indicate the end of the file transfer
sock.sendto(str.encode("Now"), (host, port))

# Close the file and socket
f.close()
sock.close()
