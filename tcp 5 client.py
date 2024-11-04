import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()
port = 9999

# Connection to hostname on the port
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

# Close the socket connection
s.close()

# Print the received time
print("The time got from the server is %s" % tm.decode('ascii'))
