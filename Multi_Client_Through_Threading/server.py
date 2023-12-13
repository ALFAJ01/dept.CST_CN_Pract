import socket
from datetime import datetime
import threading

host = "localhost"
port = 9990

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []  # List to keep track of connected clients

def bind_ser():
    try:
        server_sock.bind((host, port))
        server_sock.listen(100)
        print(f"Server is listening on IP: {host} and Port: {port}")
    except socket.error as msg:
        print("Server socket binding threw an error" + str(msg) + "\n" + "Retrying ....")
        bind_ser()

def con_accept():
    while True:
        client, addr = server_sock.accept()
        print(f"Connection has been established with client IP {str(addr[0])} and port is {str(addr[1])}")

        clients.append(client)
        client_thread = threading.Thread(target=send_response, args=(client,))
        client_thread.daemon = True
        client_thread.start()

def send_response(client):
    wcmsg = "Welcome to the server"
    client.sendall(wcmsg.encode("utf-8"))

    while True:
        try:
            command = client.recv(1024).decode("utf-8")

            if command.lower() == "day":
                response = datetime.now().strftime("%A")
            elif command.lower() == "date":
                response = datetime.now().strftime("%y-%m-%d")
            elif command.lower() == "time":
                response = datetime.now().strftime("%H:%M:%S")
            elif command.lower() == "quit" or command.lower() == "exit":
                client.close()
                clients.remove(client)
                break
            else:
                response = "You entered an invalid command"

            client.sendall(response.encode("utf-8"))
        except Exception as e:
            print(f"Error handling client: {e}")
            clients.remove(client)
            break

bind_ser()

# Start a thread to accept incoming connections
accept_thread = threading.Thread(target=con_accept)
accept_thread.daemon = True
accept_thread.start()

# Keep the main thread running
while True:
    pass

