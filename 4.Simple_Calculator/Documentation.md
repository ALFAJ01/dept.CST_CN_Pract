# **Question :** 
### Write the Server - Client Program For Where Client send mathemathical expression to the server and server send the result to the client.
# **__Program Objectivity :__**
 * #### Create a server-client application that allows multiple clients to connect and evaluate mathematical expressions.
 * #### The server handles client connections concurrently using threads for efficient communication.
 * #### Clients can send expressions to the server, receive the calculated results, and terminate connections at will.
 # Abstract Approach:
 * #### The server utilizes sockets and threading for concurrent client handling.
 * #### Upon connection, a new thread is created for each client to manage communication independently.
 * #### Client threads:
     * Welcome the client.
     * Enter a loop to receive expressions, evaluate them, and send back results.
     * Handle invalid expressions and client termination gracefully.
 * #### Clients connect to the server, receive the welcome message, enter expressions, receive results, and terminate with "quit" or "exit".
# Algorithm For this Program :
*   ## Server :
     * #### Bind the server socket to the address and port.
     * #### Start a thread to continuously accept new client connections (con_accept).
     * #### For each new client:
         * Welcome the client.
         * Create a new thread to handle the client's communication (send_response).
     * #### Enter a main loop (while True) to keep the server running.
*   ## Client:
     * #### Connect to the server.
     * #### Receive and display the welcome message.
     * #### Enter a loop:
         * Prompt the user for an expression.
         * Send the expression to the server.
         * Receive and display the response (result or error message).
         * If "quit" or "exit" entered, close the client socket and break the loop.
.
# **Required Modules and Libraries:**
* ## socket:
     * Provides functionalities for socket communication.
* ## Threading: 
    * Enables concurrent execution of client handling threads.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
```{python}
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
        elif all(c.isdigit() or c in "+-*/()" for c in command):
            try:
                result = str(eval(command))
                client.sendall(result.encode("utf-8"))
            except Exception as e:
                print(f"Error handling client: {e}")
                clients.remove(client)
                break
        else:
            result="Please enter a valid expression or type 'quit' to exit."
            client.sendall(result.encode("utf-8"))
bind_ser()

accept_thread = threading.Thread(target=con_accept)
accept_thread.daemon = True
accept_thread.start()

while True:
    pass


 ```  
*   
    * Import the socket module for socket programming and threading module for handling multiple clients concurrently.
    * Define the server's host and port.
    * Create a socket object server_sock using socket.socket().

     ```{python}
     import socket
     import threading
     host = "localhost"
     port = 9990
     server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     clients = []  

* 
    *    Define a function bind_ser() to bind the server socket to the host and port, and start listening for incoming connections. It retries if there's an error during binding.
     ```{python}
     def bind_ser():
        try:
            server_sock.bind((host, port))
            server_sock.listen(100)
            print(f"Server is listening on IP: {host} and Port: {port}")
        except socket.error as msg:
            print("Server socket binding threw an error" + str(msg) + "\n" + "Retrying ....")
            bind_ser()
 

* 
     *  Define a function con_accept() to accept incoming connections from clients. Upon connection, it prints the client's address and starts a new thread to handle the client using the send_response function.   
     ```{python}
     def con_accept():
        while True:
            client, addr = server_sock.accept()
            print(f"Connection has been established with client IP {str(addr[0])} and port is {str(addr[1])}")
    
            clients.append(client)
            client_thread = threading.Thread(target=send_response, args=(client,))
            client_thread.daemon = True
            client_thread.start()

* 
    * Define a function con_accept() to accept incoming connections from clients. It creates a new thread for each client connection and calls the send_response() function to handle client requests.
    ```{python}
     def con_accept():
     while True:
         client, addr = server_sock.accept()
         print(f"Connection has been established with client IP {str(addr[0])} and port is {str(addr[1])}")
         clients.append(client)
         client_thread = threading.Thread(target=send_response, args=(client,))
         client_thread.daemon = True
         client_thread.start()
 
* 
     *  Define a function send_response(client) to handle client requests. It sends a welcome message to the client upon connection.
     * It continuously receives commands from the client. If the command is "quit" or "exit", it closes the connection. If it's a valid mathematical expression, it evaluates and sends back the result. Otherwise, it sends an error message.
     * The server starts by binding to the host and port, then starts accepting connections in a separate thread.
    ```{python}
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
          elif all(c.isdigit() or c in "+-*/()" for c in command):
              try:
                  result = str(eval(command))
                  client.sendall(result.encode("utf-8"))
              except Exception as e:
                  print(f"Error handling client: {e}")
                  clients.remove(client)
                  break
          else:
              result = "Please enter a valid expression or type 'quit' to exit."
              client.sendall(result.encode("utf-8"))

    bind_ser()
  
    accept_thread = threading.Thread(target=con_accept)
    accept_thread.daemon = True
    accept_thread.start()

    while True:
        pass




* ## CLIENT SIDE CODE :
 ```{python} 
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
 ```
*  Import the socket module for socket programming.
* Define the server's host and port.
* Create a socket object clien_sock for the client using socket.socket().
* Connect to the server using clien_sock.connect((host, port)) and receive and print the server's welcome message upon successful connection.
    ```{python} 
    import socket
    host = "localhost"
    port = 9990
    clien_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clien_sock.connect((host, port))
    ser_response = clien_sock.recv(1024).decode("utf-8")
    print(ser_response)

* 
    * Define a function send_expression() to take input from the user, send it to the server, and print the response. It also handles the exit condition when the user types "quit" or "exit".
    ```{python} 
    def send_expression():
         print("Enter the expression of Your Problem")
         print("""Example ==> 
            If You want to add x with Y and then subtraction z;
                      then Your Expression Should Be :
                                      x+y-z
                                    and so On ..... 
             And For Exit Type -->quit or exit""")
         while True:
             command = input("Enter Your Expression :")
             clien_sock.sendall(command.encode("utf-8"))
             response = clien_sock.recv(1024).decode("utf-8")
             if response.isdigit():
                 result = "Your Expression result is : " + response
                 print(result)
             elif command.lower() == "quit" or command.lower() == "exit":
                 clien_sock.close()
                 break
             else:
                 print(response)

     send_expression()

# **Function Descriptions:**
  * ## Server-side:
       * #### bind_ser(): 
         * Binds the server socket to the specified address and port, handling errors gracefully.
       * #### con_accept():
         *  Continuously accepts new client connections, adds them to a list, and creates threads to handle them.
       * #### 
         * send_response(client): Thread function for handling individual client communication.
* ## Client-side:
     * ### send_expression():
        *  Main program loop for client interaction, including expression input, sending, receiving results, and termination.
# RESULT _ OUTPUT : 
![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/4.Simple_Calculator/Screenshot_20240122_101011.png)
