import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 12345))  # Change the port as needed
    server.listen(1)  # Allow one client to connect

    print("Waiting for a client to connect...")
    conn, addr = server.accept()
    print(f"Connected to {addr[0]} and port {addr[1]}")


    while True:
        data = conn.recv(256).decode('utf-8')
        if not data:
            break
        print(f"Client: {data}")

        message = input("You: ")
        conn.send(message.encode('utf-8'))

    conn.close()

if __name__ == "__main__":
    start_server()
