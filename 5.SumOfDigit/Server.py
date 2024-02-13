import socket
import threading

host = "localhost"
port = 9990

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []  
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
        command = client.recv(1024).decode("utf-8")
        if command.lower() in ["quit", "exit"]:
                client.sendall("Thank You .. See You soon !! ".encode("utf-8"))
                clients.remove(client)
                client.close()
                print(f"{client} Close the connection")
                break
        elif all(c.isdigit() for c in command):
            try:
                result=sum(int(c) for c in command)
                client.sendall(str(result).encode("utf-8"))
            except Exception as e:
                print(f"Error handling client: {e}")
                clients.remove(client)
                break
        else:
            result="Please enter a valid String of Digits or type 'quit' to exit."
            client.sendall(result.encode("utf-8"))
bind_ser()

accept_thread = threading.Thread(target=con_accept)
accept_thread.daemon = True
accept_thread.start()

while True:
    pass

