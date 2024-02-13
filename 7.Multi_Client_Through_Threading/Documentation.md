# **Question :** 
### Demostrate the simple Server - Client Program For handaling the multiple client.
# **__Program Objectivity :__**
 * ####      Create a server-client application for handle multiple client by simple providing the simple server - client interface like day, date and time information upon user request.
 * #### The server listens for client connections and responds to commands to obtain the current day, date, or time.
 * #### The client allows users to input specific commands to retrieve the desired information and displays the received responses.
 # Abstract Approach:
 * #### The server uses sockets to listen for incoming client connections on a specific port.
 * #### When a client connects, a new thread is created to handle multiple client communication.
 * #### Clients send commands (day, date, time) to the server, which processes them and sends back the corresponding information.
 * #### Commands like "quit" or "exit" terminate the connection.
# Algorithm For this Program :
*   ## Server :
     * #### Bind the server socket to the address and port.
     * #### Start a thread for accepting client connections.
     * #### In the connection acceptance thread:
         * Accept a new client connection.
         * Add the client's socket to the client list.
         * Create a new thread for handling messages from this client.
     * #### **In the message handling thread:**
         * #### Send a welcome message to the client.
         * #### Continuously receive commands from the client.
         * #### Process the command:
             * If "day", format and send the current day of the week.
             * If "date", format and send the current date.
             * If "time", format and send the current time.
             * If "quit" or "exit", close the connection and remove the client.
             * For invalid commands, send an error message.
         * #### Send the response to the client.
*   ## Client:
     * #### Create a socket and connect to the server's address and port.
     * #### Receive and print the welcome message sent by the server.
     * #### Enter a loop:
         * Prompt the user for a command (day, date, time, or quit/exit).
         * Send the command to the server.
         * Receive and display the server's response.
         * Check if the command was "quit" or "exit".
     * #### If user wants to exit, close the client socket and terminate the program.

# **Required Modules and Libraries:**
* ## socket:
     * Provides functionalities for socket communication.
* ## Threading: 
    * Enables concurrent execution of multiple client handling threads.
* ## datetime:
   * Offers tools for working with dates and times.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
```{python}
import socket
from datetime import datetime
import threading
import os

host = "localhost"
port = 9990

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []  # List to keep track of connected clients

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
        try:
            command = client.recv(1024).decode("utf-8")

            if command.lower() == "day":
                response = datetime.now().strftime("%A")
            elif command.lower() == "date":
                response = datetime.now().strftime("%y-%m-%d")
            elif command.lower() == "time":
                response = datetime.now().strftime("%H:%M:%S")
            elif command.lower() == "quit" or command.lower() == "exit":
                client.close()
                clients.remove(client)
                break
            else:
                response = "You entered an invalid command"

            client.sendall(response.encode("utf-8"))
        except Exception as e:
            print(f"Error handling client: {e}")
            clients.remove(client)
            break

bind_ser()

con_accept()

 ```  
*   
    * Import necessary modules: socket for socket programming, datetime for getting current date and time, threading for multi-threading support, and os for operating system related functions.
     ```{python}
     import socket
     from datetime import datetime
     import threading
     import os
     host = "localhost"
     port = 9990
     server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     clients = []  # List to keep track of connected clients
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
     *  Define a function con_accept() to accept incoming connections from clients. It creates a new thread for each client connection and calls the send_response() function to handle client requests..    
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
    * Define a function send_response(client) to handle client requests. It sends a welcome message to the client upon connection and continuously receives commands from the client. Based on the command received, it sends back the current day, date, or time, or closes the connection if the command is "quit" or "exit".
    ```{python}
    def send_response(client):
         wcmsg = "Welcome to the server"
         client.sendall(wcmsg.encode("utf-8"))
     
         while True:
             try:
                 command = client.recv(1024).decode("utf-8")
     
                 if command.lower() == "day":
                     response = datetime.now().strftime("%A")
                 elif command.lower() == "date":
                     response = datetime.now().strftime("%y-%m-%d")
                 elif command.lower() == "time":
                     response = datetime.now().strftime("%H:%M:%S")
                 elif command.lower() == "quit" or command.lower() == "exit":
                     client.close()
                     clients.remove(client)
                     break
                 else:
                     response = "You entered an invalid command"
     
                 client.sendall(response.encode("utf-8"))
             except Exception as e:
                 print(f"Error handling client: {e}")
                 clients.remove(client)
                 break

* 
     *  Bind the server socket and start accepting client connections. The server continues to run and accept connections indefinitely.
    ```{python}
     bind_ser()
     con_accept()

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
while  True:
    command=input("Enter the command for Day -> day |Date -> date |Time -> time and Exit -> quit or exit: ")
    clien_sock.sendall(command.encode("utf-8"))
    response=clien_sock.recv(1024).decode("utf-8")
    print(response)
    if  command.lower() == "quit" or command.lower() == "exit":
        clien_sock.close()
        break
 ```
 * 
    *  Import the socket module for socket programming. Define the server's host and port, and create a socket object (clien_sock) for the client. Connect to the server and receive and print the server's welcome message upon successful connection.
    ```{python} 
    import socket
    host = "localhost"
    port = 9990
    clien_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect with the server
    clien_sock.connect((host, port))
    ser_response = clien_sock.recv(1024).decode("utf-8")
    print(ser_response)

* 
    * Enter a loop to continuously take input from the user. Send the command to the server and receive and print the response. If the user enters "quit" or "exit", close the client socket and break out of the loop.
    ```{python} 
    while True:
         command = input("Enter the command for Day -> day | Date -> date | Time -> time and Exit -> quit or exit: ")
         clien_sock.sendall(command.encode("utf-8"))
         response = clien_sock.recv(1024).decode("utf-8")
         print(response)
         if command.lower() == "quit" or command.lower() == "exit":
             clien_sock.close()
             break
# **Function Descriptions:**
  * ## Server-side:
    * **bind_ser:**
      *  Binds the server socket to the specified address and port, handling errors gracefully.
    * **con_accept:**
      *  Continuously listens for new connections, accepts them, adds them to the client list, and creates threads for message handling.
    * **send_response:** 
      * Welcomes new clients, receives and processes their commands, sends back the requested date or time information, and handles invalid commands and disconnections.
  * ## Client-side:
     * **Main program loop:**
       * Continuously prompts the user for commands, sends them to the server, displays received responses, and terminates the connection upon receiving "quit" or "exit" from the server.
        
# RESULT _ OUTPUT : 
 ![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/7.Multi_Client_Through_Threading/Screenshot_20240122_102935.png)
