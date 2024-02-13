# **Question :** 
### Demostrate the simple Server - Client Program For Display the Day , date and time to the client Display.
# **__Program Objectivity :__**
  * ####     Create a server-client application that provides date and time information upon user request.
  * #### The server listens for client connections, receives commands for date or time information, and sends back the corresponding response.
  * #### The client allows users to input commands to retrieve the desired information and displays the received responses.
 # Abstract Approach:
 * #### The server uses sockets to listen for client connections on a specific port.
 * #### Upon connection, the server welcomes the client and enters a loop:
    * Receives a command (day, date, time, quit/exit) from the client.
    * Processes the command:
         * If "day", format and send the current day of the week.
         * If "date", format and send the current date.
         * If "time", format and send the current time.
         * If "quit" or "exit", close the connection and break the loop.
         * For invalid commands, send an error message.
    * The client connects to the server, receives the welcome message, prompts for commands, sends them to the server, receives and displays the responses, and allows termination with "quit" or "exit".
# Algorithm For this Program :
*   ## Server :
     * #### Bind the server socket to the address and port.
     * #### Accept a new client connection.
     * #### Welcome the client.
     * #### Enter a loop:
         * Receive a command from the client.
         * If "quit" or "exit", close the connection and break the loop.
         * Process the command and send the appropriate response.

*   ## Client:
     * #### Create a client socket and connect to the server.
     * #### Receive and display the welcome message.
     * #### Enter a loop:
         * Prompt the user for a command.
         * Send the command to the server.
         * Receive and display the response.
         * If "quit" or "exit" entered, close the client socket and break the loop.

# **Required Modules and Libraries:**
* ## socket:
     * Provides functionalities for socket communication.
* ## datetime:
   * Offers tools for working with dates and times.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
```{python}
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

 ```  
*   
    * Import the necessary module socket for socket programming and datetime for getting current date and time.
    * Define the server's host and port.
    * Create a socket object server_sock using socket.socket().
    * Define a function bind_ser() to bind the server socket to the host and port and start listening for incoming connections. It retries if there's an error during binding.
     ```{python}
     import socket
     from datetime import datetime
     host = "localhost"
     port = 9990  
     # Create a socket object from socket module
     server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     # Bind the server_sock object with host and port
     def bind_ser():
         try:
             server_sock.bind((host, port))
             server_sock.listen(1)
             print(f"Server is listening on IP: {host} and Port: {port}")
         except socket.error as msg:
             print("Server socket Binding threw an error" + str(msg) + "\n" + "Retrying ....")
             bind_ser()

* 
    *   Define a function con_accept() to accept incoming connections from clients. Upon connection, it sends a welcome message to the client and calls send_response(clien) to handle client requests.
    * Define a function send_response(clien) to handle client requests. It continuously receives commands from the client. Based on the command received, it prepares a response: current day, date, or time. If the command is "quit" or "exit", it closes the connection. Otherwise, it sends the response back to the client.
     ```{python}
    def con_accept():
    clien, addr = server_sock.accept()
    print(f"Connection has been established with client IP {str(addr[0])} and port is {str(addr[1])}")
    send_response(clien)
    def send_response(clien):
        wcmsg = "Welcome to the server"
        clien.sendall(wcmsg.encode("utf-8"))
        while True:
            command = clien.recv(1024).decode("utf-8")
            if command.lower() == "day":
                response = datetime.now().strftime("%A")
            elif command.lower() == "date":
                response = datetime.now().strftime("%y-%m-%d")
            elif command.lower() == "time":
                response = datetime.now().strftime("%H:%M:%S")
            elif command.lower() == "quit" or command.lower() == "exit":
                clien.close()
                break
            else:
            response = "You Entered an invalid Command"
            clien.sendall(response.encode("utf-8"))
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
    *  Import the socket module for socket programming.
    * Define the server's host and port.
    * Create a socket object clien_sock for the client using socket.socket().
    * Connect to the server using clien_sock.connect((host, port)) and receive and print the server's welcome message upon successful connection.
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
    * Enter a loop to continuously take input from the user.
    * Send the command to the server using clien_sock.sendall(command.encode("utf-8")) and receive the response from the server using response = clien_sock.recv(1024).decode("utf-8").
    * Print the response received from the server.
    * If the user enters "quit" or "exit", close the client socket using clien_sock.close() and break out of the loop.
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
     * **bind_ser():** 
        *  Binds the server socket to the specified address and port, handling errors gracefully.
     * **con_accept():**
        * Accepts a new client connection and passes the client socket to send_response.
     * **send_response(clien):**
         * Welcomes the client, enters a loop to receive commands, processes them, sends responses, and handles termination.
  * ## Client-side:
     * **Main program loop:**
       * Continuously prompts the user for commands, sends them to the server, displays received responses, and terminates the connection upon receiving "quit" or "exit" from the server.
        
# RESULT _ OUTPUT : 
![RESULT](/home/mr./Downloads/NBU_MSC/!st_Sem/Practical_Paper/Computer_Network/BroadcastMessge/Screenshot_20240121_164139.png)