# **Question :** 
### Write the Server - Client Program For Where Client send group of string and server counting the Character and send it to the client .
# **__Program Objectivity :__**
 * ####      The server functionality to analyze and count the occurrences of digits, uppercase and lowercase letters, spaces, and special characters in messages sent by clients and send it to the client.
 # Abstract Approach:
 * #### The server uses sockets to listen for incoming client connections on a specific port.
* #### When a client connects, a new thread is created to handle its communication.
* #### Clients send messages to the server, which analyzes them for character types and also count the total character.
* #### The server sends back a detailed breakdown of character counts to the client.
* #### Clients can leave or disconnect from server by sending a "quit" or "exit" message.
# Algorithm For this Program :
*   ## Server :
     * #### Create a socket and bind it to a specific port.
     * #### Continuously listen for incoming connections.
     * #### __In the connection acceptance thread:__
         * ##### Accept a new client connection.
         * ##### Add the client's socket to the client list.
         * ##### Create a new thread for handling messages from this client.
     * #### __In the message handling thread:__
        * ##### Send a welcome message to the client.
        * ##### Continuously receive messages from the client.
        * ##### Analyze the message to count digits, letters (uppercase and lowercase), spaces, and special characters.
        * ##### Construct a response string with the detailed character breakdown.
        * #####  Send the response to the client.
        * ##### If the message is "quit" or "exit", broadcast a goodbye message and close the connection.
*   ## Client:
     * #### Create a socket and connect to the server's address and port.
     * #### Receive and print the welcome message sent by the server.
     * #### Start a thread for sending messages to the server.
     * #### In the message sending thread:
         * #### Continuously prompt the user for input.
         * #### end the entered message to the server.
         * #### Receive and display the server's response with the character analysis.
     * #### Check if the user entered "quit" or "exit".
     * #### If user wants to exit, close the client socket and terminate the program.
     * #### Close the client socket.
# **Required Modules and Libraries:**
* ## socket:
     * Provides functionalities for socket communication.
* ## Threading: 
    * Enables concurrent execution of client handling threads.
* ## string: 
     *  Offers character classification functions.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
```{python}
import socket
import threading
import string 
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
        Digit=0
        lowlet=0
        uplet=0
        special=0
        spac=0
        command = client.recv(1024).decode("utf-8")
        if command.lower() in ["quit", "exit"]:
                client.sendall("Thank You .. See You soon !! ".encode("utf-8"))
                clients.remove(client)
                client.close()
                print(f"{client} Close the connection")
                break
        for c in command:               
                if c.isdigit():
                     Digit+=1
                elif c.islower():
                     lowlet+=1
                elif c.isupper():
                     uplet+=1
                elif c==" ":
                     spac+=1
                else :
                    special+=1 
        totalcharacter=Digit+lowlet+uplet+special
        result=f" String Have total {totalcharacter} and Have Digit: {Digit} , Uppercase letter: {uplet},Lowercase letter :{lowlet}, Special Character :{special} and space: {spac} "
        client.sendall(result.encode("utf-8"))

bind_ser()

accept_thread = threading.Thread(target=con_accept)
accept_thread.daemon = True
accept_thread.start()

while True:
    pass


 ```  
*   
    * Import necessary modules: socket for socket programming, threading for multi-threading support, and string for string operations.
     ```{python}
     import socket
     import threading 
     import string 
* 
    *    Define the server's host and port. Create a socket object (server_sock) for the server and initialize an empty list clients to keep track of connected clients.
     ```{python}
     host = "localhost"
     port = 9990
     server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     clients = []  

* 
     *  Define a function bind_ser() to bind the server socket to the host and port, and start listening for incoming connections. It retries if there's an error during binding.    
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
     *  Define a function send_response(client) to handle client requests. It sends a welcome message to the client upon connection and continuously receives commands from the client. If the command is "quit" or "exit", it closes the connection with the client.
    ```{python}
    def send_response(client):
    wcmsg = "Welcome to the server"
    client.sendall(wcmsg.encode("utf-8"))

    while True:
        Digit=0
        lowlet=0
        uplet=0
        special=0
        spac=0
        command = client.recv(1024).decode("utf-8")
        if command.lower() in ["quit", "exit"]:
                client.sendall("Thank You .. See You soon !! ".encode("utf-8"))
                clients.remove(client)
                client.close()
                print(f"{client} Close the connection")
                break

* 
    * The function then analyzes the received command to count the number of digits, lowercase letters, uppercase letters, special characters, and spaces in the string. It sends the result back to the client.
    ```{python}
            for c in command:               
                if c.isdigit():
                     Digit+=1
                elif c.islower():
                     lowlet+=1
                elif c.isupper():
                     uplet+=1
                elif c==" ":
                     spac+=1
                else :
                    special+=1 
        totalcharacter=Digit+lowlet+uplet+special
        result=f" String Have total {totalcharacter} and Have Digit: {Digit} , Uppercase letter: {uplet},Lowercase letter :{lowlet}, Special Character :{special} and space: {spac} "
        client.sendall(result.encode("utf-8"))

* 
    * Bind the server socket, start accepting client connections in a separate thread, and keep the main thread running indefinitely.

    ```{python}
     bind_ser()

     accept_thread = threading.Thread(target=con_accept)
     accept_thread.daemon = True
     accept_thread.start()

     while True:
         pass

* ## CLIENT SIDE CODE :
 ```{python} 
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
 ```
*  Similar to the server-side code, the socket is imported for socket programming.
    ```{python} 
    import socket
* 
    * Define the server's host and port, and create a socket object (clien_sock) for the client.
    ```{python} 
    host = "localhost"
    port = 9990
    clien_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
* 
    * Attempt to connect to the server. Receive and print the server's welcome message upon successful connection.
     ```{python} 
    try:
        clien_sock.connect((host, port))
        ser_response = clien_sock.recv(1024).decode("utf-8")
        print(ser_response)

* 
    * Define a function send_expression() to continuously take input from the user, send it to the server, and receive and print the server's response. If the user enters "quit" or "exit", the function exits.
     ```{python}
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

* 
    * THandle any exceptions that may occur during the connection process. Finally, close the client socket.
    ```{python}
    except Exception as e:
      print(f"An error occurred: {e}")
    finally:
        clien_sock.close()
# **Function Descriptions:**
  * ## Server-side:
       * #### bind_ser: 
          *  Binds the server socket to the specified address and port, handling errors gracefully.
    * #### con_accept: 
       * Continuously listens for new connections, accepts them, adds them to the client list, and creates threads for message handling.
    * #### send_response: 
       * Welcomes new clients, analyzes their messages, counts character types, and sends detailed feedback.
* ## Client-side:
     * ### send_expression: 
         * Continuously prompts the user for messages, sends them to the server, and displays received responses.
# RESULT _ OUTPUT : 
 ![RESULT](/home/mr./Downloads/NBU_MSC/!st_Sem/Practical_Paper/Computer_Network/BroadcastMessge/Screenshot_20240121_164139.png)