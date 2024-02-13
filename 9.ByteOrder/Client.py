import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9990))

    # Receive byte order information from the server
    byte_order = client.recv(1024).decode('utf-8')

    # Display the byte order information
    print(f"The byte order of the server is: {byte_order}")
    command=input("For Exit Write quit /Exit :")
    client.sendall(command.encode("utf-8"))
    if command == "quit":
        client.close()
        exit()

if __name__ == "__main__":
    start_client()
