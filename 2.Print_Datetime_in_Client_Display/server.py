import socket
from datetime import datetime
host="localhost"
port=9990
#Create a socket object from socket module
server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Bind the server_sock object with host and port 
def bind_ser():
    try:
        server_sock.bind((host,port))
        server_sock.listen(1)
        print(f"Server is lisening on IP: {host} and Port : {port}")
    except socket.error as msg:
        print("Server socket Binding through an error" +str(msg)+"/n"+"Retrying ....")
        bind_ser()
def con_accept():
    clien,addr=server_sock.accept()
    print(f"Connection hasbeen establised with client ip {str(addr[0])} and port is {str(addr[1])}")
    send_response(clien)
def send_response(clien):
    wcmsg="Wellcome to the server"
    clien.sendall(wcmsg.encode("utf-8"))
    while True:
        command=clien.recv(1024).decode("utf-8")
        if command.lower()=="day":
            response=datetime.now().strftime("%A")
        elif command.lower()=="date":
            response=datetime.now().strftime("%y-%m-%d")
        elif command.lower()=="time":
            response=datetime.now().strftime("%H:%M:%S")
        elif  command.lower() == "quit" or command.lower() == "exit":
            clien.close()
            break
        else:
            response="You Entered an invalid Command"
        clien.sendall(response.encode("utf-8"))
bind_ser()
con_accept()
