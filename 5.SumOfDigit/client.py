import socket
host="localhost"
port=9990
clien_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect with the server
clien_sock.connect((host,port))
ser_response=clien_sock.recv(1024).decode("utf-8")
print(ser_response)
def send_expression():
    print("For Exit ==>quit or exit")
    while  True:
        command=input("Enter Your Strings of Digits : ")
        clien_sock.sendall(command.encode("utf-8"))
        response=clien_sock.recv(1024).decode("utf-8")
        if response.isdigit():
             result="Your Strings All Didgit Sum is : "+ response
             print(result)
        elif  command.lower() == "quit" or command.lower() == "exit":
                clien_sock.close()
                break
        else:
             print(response)
send_expression()