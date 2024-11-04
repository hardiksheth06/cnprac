import socket

# Server configuration
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3333         # Port to listen on

# Create a TCP socket using context manager
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the specified host and port
    s.bind((HOST, PORT))
    
    # Listen for incoming connections (with a default backlog of 1)
    s.listen()
    print("Server is listening on {}:{}".format(HOST, PORT))

    # Accept a connection from a client
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        
        # Continuously listen for messages from the client
        while True:
            # Receive data from the client
            data = conn.recv(1024).decode()
            print('Client says:', data)
            
            # If the client sends 'stop', break the loop
            if data == 'stop':
                break
            
            # Get a response message from the server user
            str2 = input("Enter your message: ")
            
            # Send the response to the client
            conn.sendall(str2.encode())
