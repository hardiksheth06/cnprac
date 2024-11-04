import socket

# Client configuration
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 3333         # The port used by the server

# Create a TCP socket using context manager
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

    # Communication loop
    while True:
        # Get a message from the client user
        message = input("Enter your message: ")
        
        # Send the message to the server
        s.sendall(message.encode())
        
        # If the message is 'stop', break the loop
        if message == 'stop':
            break
        
        # Receive a response from the server
        data = s.recv(1024).decode()
        print('Server says:', data)
