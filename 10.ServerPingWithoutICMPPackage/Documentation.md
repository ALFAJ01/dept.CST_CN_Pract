# Question:
  * Write a server - client program for ping a host and recived and acknowledgement text whether the host is rechable or not 
# CODE :
  * ## SERVER SIDE CODE :
    ```{python} 
     import socket

     def server():
         host = 'localhost'
         port = 12345
     
         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server_socket.bind((host, port))
         server_socket.listen(1)
     
         print(f"Server listening on {host}:{port}")
     
         client_socket, addr = server_socket.accept()
         print(f"Connection from {addr}")
     
         while True:
             data = client_socket.recv(1024).decode()
             if not data:
                 break
     
             print(f"Received: {data}")
     
             # Send acknowledgment back to the client
             client_socket.send("Ping Acknowledged".encode())

         client_socket.close()
         server_socket.close()

     if __name__ == "__main__":
         server()
    ```
    * ## CLIENT SIDE CODE :
      ```{python} 
      import socket

      def client():
            host = 'localhost'
            port = 12345

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           client_socket.connect((host, port))

         while True:
                message = input("Enter message to ping the server (type 'exit' to quit): ")
                if message.lower() == 'exit':
                    break

        client_socket.send(message.encode())
             response = client_socket.recv(1024).decode()
      
                print(f"Server response: {response}")
      
           client_socket.close()

      if __name__ == "__main__":
           client()

      ```
# RESULT _ OUTPUT : 
![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/10.ServerPingWithoutICMPPackage/Screenshot_20240122_104744.png)
