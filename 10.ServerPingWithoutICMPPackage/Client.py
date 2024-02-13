import socket

def client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message to ping the server (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()

        print(f"Server response: {response}")

    client_socket.close()

if __name__ == "__main__":
    client()
