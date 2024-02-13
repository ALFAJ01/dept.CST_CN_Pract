# **Question :** 
### Demostrate the simple Server - Client Program Form Where the client send to the server a set of number and server send it to the client the total sum of the send Number of every individual digit.
# **__Program Objectivity :__**
  * ####     This program creates a server-client application where the server calculates the sum of digits in a string sent by the client.
  * #### The server handles multiple clients concurrently using threads.
  * #### Clients can send strings of digits, receive the sum, and terminate the connection at will.
 # Abstract Approach:
 * #### The server uses sockets and threading for concurrent client handling.
 * #### Upon connection, a new thread is created for each client to manage communication independently.
 * #### Client threads:
     * Welcome the client.
     * Enter a loop to receive strings, calculate the sum of digits, and send back results.
     * Handle invalid input and client termination gracefully.
 * #### Clients connect to the server, receive the welcome message, enter digit strings, receive sums, and terminate with "quit" or "exit".
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
         * Prompt the user for a string of digits.
         * Send the string to the server.
         * Receive and display the response (sum or error message).
         * If "quit" or "exit" entered, close the client socket and break the loop.

# **Required Modules and Libraries:**
* ## socket:
     * Provides functionalities for socket communication.
* ## threading: 
     * Enables the creation and management of threads for concurrent tasks.

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
        elif all(c.isdigit() for c in command):
            try:
                result=sum(int(c) for c in command)
                client.sendall(str(result).encode("utf-8"))
            except Exception as e:
                print(f"Error handling client: {e}")
                clients.remove(client)
                break
        else:
            result="Please enter a valid String of Digits or type 'quit' to exit."
            client.sendall(result.encode("utf-8"))
bind_ser()

accept_thread = threading.Thread(target=con_accept)
accept_thread.daemon = True
accept_thread.start()

while True:
    pass

 ```  
*   
    * The server initializes a socket using socket.socket() with IPv4 addressing and TCP protocol.
    * It defines the host and port to bind the server socket.
    * A function bind_ser() is defined to bind the server socket to the host and port, and start listening for incoming connections. It handles errors that may occur during socket binding.

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
     
     
* 
    *  **con_accept()** is a function that continuously accepts incoming connections from clients.
    * Upon accepting a connection, it prints the client's IP address and port, adds the client socket to the list of clients, and starts a new thread to handle the client using the send_response function.
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
    *   **send_response(client)** is a function that handles client requests.
    * It sends a welcome message to the client upon connection.
    * It continuously receives commands from the client. If the command is "quit" or "exit", it closes the connection. If it consists only of digits, it calculates the sum and sends it back. Otherwise, it sends an error message.
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
            elif all(c.isdigit() for c in command):
                try:
                    result = sum(int(c) for c in command)
                    client.sendall(str(result).encode("utf-8"))
                except Exception as e:
                    print(f"Error handling client: {e}")
                    clients.remove(client)
                    break
            else:
                result = "Please enter a valid String of Digits or type 'quit' to exit."
                client.sendall(result.encode("utf-8"))

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
 ```
 * 
    *  The client initializes a socket using socket.socket() with IPv4 addressing and TCP protocol.
    * It defines the server's host and port to connect to.
    * It connects to the server using clien_sock.connect((host, port)) and receives and prints the server's welcome message upon successful connection.
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
    * It defines a function send_expression() to take input from the user, send it to the server, and print the response.
    * It continuously prompts the user to enter a string of digits.
    * If the response from the server is a digit, it prints the sum of the digits. If the command is "quit" or "exit", it closes the connection. Otherwise, it prints the server's response.
    ```{python} 
    def send_expression():
        print("For Exit ==> quit or exit")
        while True:
            command = input("Enter Your Strings of Digits : ")
            clien_sock.sendall(command.encode("utf-8"))
            response = clien_sock.recv(1024).decode("utf-8")
            if response.isdigit():
                result = "Your Strings All Digit Sum is : " + response
                print(result)
            elif command.lower() == "quit" or command.lower() == "exit":
                clien_sock.close()
                break
            else:
                print(response)
    send_expression()

# **Function Descriptions:**
  * ## Server-side:
     * **bind_ser():**
        *  Binds the server socket to the specified address and port, handling errors gracefully.
     * **con_accept():** 
         * Continuously accepts new client connections, adds them to a list, and creates threads to handle them.
     * **send_response(client):** 
         * Thread function for handling individual client communication.
  * ## Client-side:
     * **send_expression():**
         *  Main program loop for client interaction, including string input, sending, receiving results, and termination.
# RESULT _ OUTPUT : 
![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/5.SumOfDigit/Screenshot_20240122_100451.png)
