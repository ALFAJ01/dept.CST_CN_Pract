import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))  # Replace 'server_ip' with the server's IP address

    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))

        data = client.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Server: {data}")

    client.close()

if __name__ == "__main__":
    start_client()
