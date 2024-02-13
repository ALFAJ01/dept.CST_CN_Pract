# Question :
   * Write the Server - Client  Program for determine the byte order.
# Program Objective:
* The objective of this Python program is to establish a server-client interaction where the server provides information about its byte order to the client. The server sends whether it is in little-endian or big-endian order, and the client displays this information. The program also allows the client to exit the connection gracefully.

# Abstract Approach:
* To achieve the objective, the following approach is taken:
     * Socket Module:
         * The socket module is used for network communication between the server and client.
     * Byte Order:
         * The sys module is used to determine the byte order of the server.
     * Server:
        *  The server has two main functions: get_byte_order and start_server.
        *  get_byte_order(): Determines the byte order of the server using the sys module.
        *  start_server(): Creates a server socket, binds it to a specified host and port, and listens for incoming connections. It then sends the byte order information to the connected client.
     * Client:
        *  The client has one function: start_client.
        *  start_client(): Creates a client socket, connects to the server, receives the byte order information, and displays it. The client also has the option to exit the connection.

# Required Modules and Function Details:
*  Server Side (server.py):
    *  Imports:
        *  socket: For network communication.
        *  sys: For determining byte order.
    *  Functions:
        *  get_byte_order(): Determines the byte order of the server using the sys module.
        *  start_server(): Creates a server socket, binds it to a specified host and port, and listens for incoming connections. It sends the byte order information to the connected client.

*  Client Side (client.py):
    *  Imports:
        *  socket: For network communication.
    *  Functions:
        *  start_client(): Creates a client socket, connects to the server, receives the byte order information, and displays it. The client also has the option to exit the connection.

#  Usage of Modules and Functions:
*  Socket Module (socket):
    *  Used for creating server and client socket objects.
    *  Enables communication between the server and clients.
*  sys Module:
    *  Used to determine the byte order of the server.
*  Functions:
    *  get_byte_order(): Determines the byte order of the server.
    *  start_server(): Creates a server socket, binds it to a specified host and port, and sends the byte order information to the connected client.
    *  start_client(): Creates a client socket, connects to the server, receives the byte order information, and displays it. The client also has the option to exit the connection.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
```{python}
import socket
import sys

def get_byte_order():
    if sys.byteorder == 'little':
        return 'Little-endian'
    else:
        return 'Big-endian'

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9990))
    server.listen(1)
    print("Server listening on port 9990")

    while True:
        client_socket, client_addr = server.accept()
        print(f"Accepted connection from {client_addr}")

        # Get byte order of the server
        byte_order = get_byte_order()

        # Send byte order information to the client
        client_socket.send(byte_order.encode('utf-8'))
        msg=client_socket.recv(1024)
        if msg.decode("utf-8").lower()== "quit" or "exit":
            client_socket.close()
            print("Connection closed")

if __name__ == "__main__":
    start_server()
```
*   
    *  Imports:
        *  import socket: Imports the socket module for network communication.
        *  import sys: Imports the sys module for system-related information.
    * Function get_byte_order():
        *  Defines a function get_byte_order() that determines the byte order of the system.
        *  Checks if the byte order is 'little' (little-endian) and returns 'Little-endian'.
        *  Otherwise, it returns 'Big-endian'.
    ```{python}
     def get_byte_order():
         if sys.byteorder == 'little':
             return 'Little-endian'
         else:
             return 'Big-endian'
*   
    *  Function start_server():
        *  Defines a function start_server() responsible for setting up the server.
        *  Creates a socket (socket.AF_INET for IPv4, socket.SOCK_STREAM for TCP).
        *  Binds the server to the host ('localhost') and port 9990.
        *  Listens for incoming connections with a backlog of 1.
        *  Prints a message indicating that the server is listening on port 9990.
    *  Server Loop:
        *  Uses a while True loop to continuously accept incoming connections.
        *  When a client connects, it prints a message indicating the acceptance and the client's address.
    *  Byte Order Retrieval and Sending:
        *  Calls the get_byte_order() function to determine the byte order of the server.
        *  Sends the byte order information to the connected client using client_socket.send().
    *  Client Communication:
        *  Receives a message (msg) from the client with a maximum length of 1024 bytes.
        *  Checks if the received message, converted to lowercase, is either "quit" or "exit."
        *  If the condition is met, it closes the client connection and prints a message indicating the closure.
    *  Main Block:
        *  In the main block (if __name__ == "__main__":), it calls the start_server() function to initiate the server.
    ```{python}
     def start_server():
         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server.bind(('localhost', 9990))
         server.listen(1)
         print("Server listening on port 9990")

         while True:
             client_socket, client_addr = server.accept()
             print(f"Accepted connection from {client_addr}")
     
        # Get byte order of the server
             byte_order = get_byte_order()
     
             # Send byte order information to the client
             client_socket.send(byte_order.encode('utf-8'))
             msg=client_socket.recv(1024)
             if msg.decode("utf-8").lower()== "quit" or "exit":
                 client_socket.close()
                 print("Connection closed")
     
     if __name__ == "__main__":
         start_server()
# CODE EXPAIN :
* **CLIENT SIDE CODE :**
```{python} 
import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9990))

    # Receive byte order information from the server
    byte_order = client.recv(1024).decode('utf-8')

    # Display the byte order information
    print(f"The byte order of the server is: {byte_order}")
    command=input("For Exit Write quit /Exit :")
    client.sendall(command.encode("utf-8"))
    if command == "quit":
        client.close()
        exit()

if __name__ == "__main__":
    start_client()
```

*   
    *   Imports:
        * import socket: Imports the socket module for network communication.
    ```{python}
     import socket'
*   
    *  Function start_client():
        * Defines a function start_client() responsible for setting up the client.
        * Creates a client socket (socket.AF_INET for IPv4, socket.SOCK_STREAM for TCP).
        * Connects the client socket to the server at 'localhost' and port 9990.
    ```{python}
     def start_client():
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         client.connect(('localhost', 9990))
*   
    *   Byte Order Reception:
         *  Receives a message (byte_order) from the server with a maximum length of 1024 bytes.
         * Decodes the received bytes into a UTF-8 formatted string.
    ```{python}
      byte_order = client.recv(1024).decode('utf-8') 
    
*   
    *   Display Information and User Input:
        *  Prints a message displaying the byte order information received from the server.
        *  Prompts the user to input a command for exiting.
    ```{python}
     # Display the byte order information
     print(f"The byte order of the server is: {byte_order}")
     command = input("For Exit Write quit /Exit :")
*   
    *    Command Sending:
        *  Encodes the user input command into bytes using UTF-8 and sends it to the server using client.sendall().
    ```{python}
    client.sendall(command.encode("utf-8")) 
    
*   
    *  Client Exit Handling:
        *  Checks if the user input command is "quit."
        *  If true, it closes the client connection gracefully using client.close() and exits the program using exit().
    ```{python}
    if command == "quit":
        client.close()
        exit()
*   
    *    Main Block:
        *  In the main block (if __name__ == "__main__":), it calls the start_client() function to initiate the client.
    ```{python}
    if __name__ == "__main__":
        start_client()
     ```
  # RESULT OUTPUT :
  ![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/9.ByteOrder/Screenshot_20240122_104353.png)
