import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except:
            break

def send_messages(sock):
    while True:
        message = input()
        sock.sendall(message.encode('utf-8'))
        if message.lower() == "quit" or message.lower() == "exit":
            break

def main():
    host = 'localhost'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    welcome_msg = client_socket.recv(1024)
    print(welcome_msg.decode('utf-8'))

    name = input("Enter your name: ")
    client_socket.sendall(name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    send_thread = threading.Thread(target=send_messages, args=(client_socket,), daemon=True)

    receive_thread.start()
    send_thread.start()

    send_thread.join()  # Wait for the sending thread to finish

    client_socket.close()

if __name__ == "__main__":
    main()
