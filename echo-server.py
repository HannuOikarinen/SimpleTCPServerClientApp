import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind the socket to the address and port
    s.listen()            # Enable the server to accept connections
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept()  # Wait for a client connection
    with conn:               # Use the connection in a context manager
        print(f"Connected by {addr}")  # Print the address of the connected client
        while True:
            data = conn.recv(1024)  # Receive data from the client
            if not data:
                break               # Exit loop if no data is received
            print(f"Received: {data.decode()}")  # Print received data
            conn.sendall(data)     # Echo back the received data