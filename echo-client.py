import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    message = b"Hello, world"  # Message to send
    s.sendall(message)         # Send the message to the server
    data = s.recv(1024)       # Receive response from server
    print(f"Received: {data.decode()}")  # Print received data