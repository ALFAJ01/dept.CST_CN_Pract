import socket
host="localhost"
port=9990
clien_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connect with the server
clien_sock.connect((host,port))
ser_response=clien_sock.recv(1024).decode("utf-8")
print(ser_response)
def send_expression():
    print("Enter the expression of Your Problem")
    print("""Example ==> 
       If You want to add x with Y and then subtraction z;
                 then Your Expression Should Be :
                                 x+y-z
                               and so On ..... 
        And For Exit Type -->quit or exit""")
    while  True:
        command=input("Enter Your Expression :")
        clien_sock.sendall(command.encode("utf-8"))
        response=clien_sock.recv(1024).decode("utf-8")
        if response.isdigit():
             result="Your Expression result is : "+ response
             print(result)
        elif  command.lower() == "quit" or command.lower() == "exit":
                clien_sock.close()
                break
        else:
             print(response)
send_expression()