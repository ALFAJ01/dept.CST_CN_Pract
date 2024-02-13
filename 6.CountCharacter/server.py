import socket
import threading
import string 
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
        Digit=0
        lowlet=0
        uplet=0
        special=0
        spac=0
        command = client.recv(1024).decode("utf-8")
        if command.lower() in ["quit", "exit"]:
                client.sendall("Thank You .. See You soon !! ".encode("utf-8"))
                clients.remove(client)
                client.close()
                print(f"{client} Close the connection")
                break
        for c in command:               
                if c.isdigit():
                     Digit+=1
                elif c.islower():
                     lowlet+=1
                elif c.isupper():
                     uplet+=1
                elif c==" ":
                     spac+=1
                else :
                    special+=1 
        totalcharacter=Digit+lowlet+uplet+special
        result=f" String Have total {totalcharacter} and Have Digit: {Digit} , Uppercase letter: {uplet},Lowercase letter :{lowlet}, Special Character :{special} and space: {spac} "
        client.sendall(result.encode("utf-8"))

bind_ser()

accept_thread = threading.Thread(target=con_accept)
accept_thread.daemon = True
accept_thread.start()

while True:
    pass

