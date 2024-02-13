import socket
import os
from datetime import datetime

MAX_CLIENTS_PER_PROCESS = 4

def send_response(client_socket, client_address):
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    print(f"<.......................PID: {os.getpid()} ...............>")

    wcmsg = "Welcome to the server"
    client_socket.sendall(wcmsg.encode("utf-8"))

    while True:
        try:
            command = client_socket.recv(1024).decode("utf-8")

            if command.lower() == "day":
                response = datetime.now().strftime("%A")
            elif command.lower() == "date":
                response = datetime.now().strftime("%y-%m-%d")
            elif command.lower() == "time":
                response = datetime.now().strftime("%H:%M:%S")
            elif command.lower() == "quit" or command.lower() == "exit":
                client_socket.close()
                break
            else:
                response = "You entered an invalid command"

            client_socket.sendall(response.encode("utf-8"))

        except Exception as e:
            print(f"Error handling client: {str(e)}")
            break

def handle_clients_in_process(server_socket):
    while True:  # Continuously accept clients
        client_socket, client_address = server_socket.accept()
        try:
            # Fork a child process to handle the client
            pid = os.fork()
            if pid == 0:  # Child process
                send_response(client_socket, client_address)
                os._exit(0)  # Terminate after handling the client
            else:  # Parent process
                client_socket.close()  # Close the socket in the parent
        except Exception as e:
            print(f"Error handling client: {str(e)}")

def bind_ser():
    host = "localhost"
    port = 9900

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_sock.bind((host, port))
        server_sock.listen(100)
        print(f"Server is listening on IP: {host} and Port: {port}")
        return server_sock  # Return the server socket
    except socket.error as msg:
        print("Server socket binding threw an error" + str(msg) + "\n" + "Retrying ....")
        return bind_ser()

def main():
    server_sock = bind_ser()

    while True:
        try:
            handle_clients_in_process(server_sock)
        except Exception as e:
            print(f"Error in main loop: {str(e)}")

if __name__ == "__main__":
    main()
