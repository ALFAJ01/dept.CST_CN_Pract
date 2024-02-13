import socket
import threading

def handle_client(client_socket, client_address):
    msg = """
                    Welcome Md's Broadcasting Message Platform
                                   o    o
                                 <   __   >"""
    client_socket.sendall(msg.encode("utf-8"))
    name = client_socket.recv(32).decode('utf-8')

    while True:
        data = client_socket.recv(1024)
        if data.decode("utf-8").lower() == "quit" or data.decode("utf-8").lower() == "exit":
             data=f"{name} Exit From the Chat Server ".encode("utf-8")
             broadcast(data, client_socket, name)
             break
        message = f"{name}: {data.decode('utf-8')}"
        print(message)
        broadcast(data, client_socket, name)

    print(f"Connection with {client_address} closed.")
    client_sockets.remove(client_socket)
    client_socket.close()

def broadcast(data, sender_socket, name):
    for client_socket in client_sockets:
        try:
            if client_socket == sender_socket:
                pass
                # msg = f"You: {data.decode('utf-8')}"
                # client_socket.sendall(msg.encode('utf-8'))
            else:
                message = f"{name}: {data.decode('utf-8')}"
                client_socket.sendall(message.encode('utf-8'))
        except:
            # Remove broken connections
            client_sockets.remove(client_socket)

host = 'localhost'
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

client_sockets = []

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_sockets.append(client_socket)

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
