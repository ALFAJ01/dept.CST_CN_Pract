import socket

host = "localhost"
port = 9990
clien_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clien_sock.connect((host, port))
    ser_response = clien_sock.recv(1024).decode("utf-8")
    print(ser_response)
    def send_expression():
        print("For Exit ==> quit or exit")
        while True:
            command = input("Enter Your Strings For Character Counting: ")
            clien_sock.sendall(command.encode("utf-8"))   
            response = clien_sock.recv(1024).decode("utf-8")            
            if command.lower() == "quit" or command.lower() == "exit":
                print(response)
                break
            else :
                result = str(command) + response
                print(result)
    send_expression()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
     
    clien_sock.close()
