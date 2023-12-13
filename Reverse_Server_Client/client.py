import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9599

s.connect((host, port))

while True:
    data = s.recv(1024)
    dcdata = data.decode('utf-8')
    print(dcdata)

    user_input = input()
    if user_input == 'quit':
        s.close()
        sys.exit()
    
    if len(user_input) > 0:
        user_input_encoded = user_input.encode('utf-8')
        s.send(user_input_encoded)
        server_response = s.recv(1024).decode("utf-8")

        print(server_response)
