import socket

def server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print(f"Received: {data}")

        # Send acknowledgment back to the client
        client_socket.send("Ping Acknowledged".encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    server()
