
import socket

# Server configuration
host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 12000        # Port to listen on

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))  # Bind the socket to the specified IP and port

# Open a new file to write the received data
f = open('Myfile2.txt', 'wb')
print('New file created')

# Receive data from the client
data, addr = sock.recvfrom(1024)
while data:
    print(data)  # Display received data

    # If the received data is "Now", it indicates the end of the file
    if data.decode("utf-8") == "Now":
        break

    # Write the data to the file
    f.write(data)

    # Receive the next chunk of data
    data, addr = sock.recvfrom(1024)

print('File is successfully received!!!')

# Close the file after receiving all data
f.close()

# Open the file in read mode and display its contents
f = open('Myfile2.txt', 'r')
print(f.read())
f.close()

# Close the socket
sock.close()
print('Connection closed!')
