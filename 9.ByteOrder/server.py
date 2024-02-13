import socket
import sys

def get_byte_order():
    if sys.byteorder == 'little':
        return 'Little-endian'
    else:
        return 'Big-endian'

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9990))
    server.listen(1)
    print("Server listening on port 9990")

    while True:
        client_socket, client_addr = server.accept()
        print(f"Accepted connection from {client_addr}")

        # Get byte order of the server
        byte_order = get_byte_order()

        # Send byte order information to the client
        client_socket.send(byte_order.encode('utf-8'))
        msg=client_socket.recv(1024)
        if msg.decode("utf-8").lower()== "quit" or "exit":
            client_socket.close()
            print("Connection closed")

if __name__ == "__main__":
    start_server()
