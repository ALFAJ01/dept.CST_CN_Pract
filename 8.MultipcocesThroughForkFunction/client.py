import socket
host="localhost"
port=9900
clien_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect with the server
clien_sock.connect((host,port))
ser_response=clien_sock.recv(1024).decode("utf-8")
print(ser_response)
while  True:
    command=input("Enter the command for Day -> day |Date -> date |Time -> time and Exit -> quit or exit: ")
    clien_sock.sendall(command.encode("utf-8"))
    response=clien_sock.recv(1024).decode("utf-8")
    print(response)
    if  command.lower() == "quit" or command.lower() == "exit":
        clien_sock.close()
        break