# **Question :** 
### Write the Server - Client Program For Broadcasting the Message By multiple Client throught the Server.
# **__Program Objectivity :__**
 * ####      This program creates a simple text-based chat server and client application. The server allows multiple clients to connect and chat with each other in real-time, broadcasting messages sent by any client to all connected users.
 # Abstract Approach:
 * #### The server uses sockets to listen for incoming client connections on a specific port.
* #### When a client connects, a new thread is created to handle its communication.
* #### The client thread welcomes the new user, prompts for a nickname, and then receives and broadcasts messages.
* #### Messages are prepended with the sender's nickname for identification.
* #### Clients can leave the chat by sending a "quit" or "exit" message.
# Algorithm For this Program :
*   ## Server :
     * #### Create a socket and bind it to a specific port.
     * #### Continuously listen for incoming connections.
     * #### __When a client connects:__
         * ##### Create a new thread to handle the client.
         * ##### Pass the client's socket and address to the thread.
         * ##### Start the thread.
     * #### __In the client handling thread:__
        * ##### Send a welcome message to the client.
        * ##### Receive the client's nickname.
        * ##### **Enter a loop:**
           * ##### Receive a message from the client.
           * ##### If the message is "quit" or "exit", broadcast a goodbye message and close the connection.
           * ##### Otherwise, prepend the sender's nickname and broadcast the message to all other connected clients.
            
     * #### **When a client disconnects:**
         * #### Remove the client's socket from the list of connected clients.
*   ## Client:
     * #### Create a socket and connect to the server's address and port.
     * #### Receive and print the welcome message sent by the server.
     * #### Enter the user's nickname and send it to the server.
     * #### Create two threads:
         * #### One for receiving messages from the server (using receive_messages).
         * #### One for sending messages to the server (using send_messages).
     * #### Start both threads.
     * #### Wait for the sending thread to finish (using send_thread.join()).
     * #### Close the client socket.
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

def handle_client(client_socket, client_address):
    msg = """
                    Welcome Md's Broadcasting Message Platform
                                   o    o
                                 <   __   >"""
    client_socket.sendall(msg.encode("utf-8"))
    name = client_socket.recv(32).decode('utf-8')

    while True:
        data = client_socket.recv(1024)
        if data.decode("utf-8").lower() == "quit" or data.decode("utf-8").lower() == "exit":
             data=f"{name} Exit From the Chat Server ".encode("utf-8")
             broadcast(data, client_socket, name)
             break
        message = f"{name}: {data.decode('utf-8')}"
        print(message)
        broadcast(data, client_socket, name)

    print(f"Connection with {client_address} closed.")
    client_sockets.remove(client_socket)
    client_socket.close()

def broadcast(data, sender_socket, name):
    for client_socket in client_sockets:
        try:
            if client_socket == sender_socket:
                pass
                # msg = f"You: {data.decode('utf-8')}"
                # client_socket.sendall(msg.encode('utf-8'))
            else:
                message = f"{name}: {data.decode('utf-8')}"
                client_socket.sendall(message.encode('utf-8'))
        except:
            # Remove broken connections
            client_sockets.remove(client_socket)

host = 'localhost'
port = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

client_sockets = []

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")
    client_sockets.append(client_socket)

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
 ```  
*   
    * These lines import the necessary modules for network communication and multithreading.
     ```{python}
     import socket
     import threading 
* 
    *    handle_client function is defined to handle each client's connection and communication.
     ```{python}
      def handle_client(client_socket, client_address)
* 
     *  A welcome message is defined and sent to the client upon connection.    
     ```{python}
    msg = """
          Welcome Md's Broadcasting Message Platform
                  o  o
                 <  __  >"""
    client_socket.sendall(msg.encode("utf-8"))
* 
    * The server receives the client's name.
    ```{python}
      name = client_socket.recv(32).decode('utf-8')
* 
     *  The server continuously receives data from the client until the connection is terminated.
    ```{python}
     while True:
        data = client_socket.recv(1024)
* 
    * If the received data is "quit" or "exit", the server broadcasts a message about the client exiting from the chat server and breaks out of the loop.
    ```{python}
    if data.decode("utf-8").lower() == "quit" or data.decode("utf-8").lower() == "exit":
       data=f"{name} Exit From the Chat Server ".encode("utf-8")
       broadcast(data, client_socket, name)
       break
* 
    * Otherwise, the server prints the received message along with the sender's name and broadcasts the message to all other connected clients
    ```{python}
     message = f"{name}: {data.decode('utf-8')}"
     print(message)
     broadcast(data, client_socket, name)
* 
    * After the client disconnects, the server removes the client's socket from the list of client sockets and closes the connection.
    ```{python}
     print(f"Connection with {client_address} closed.")
     client_sockets.remove(client_socket)
     client_socket.close()
* 
    * **broadcast** function is defined to send a message to all connected clients except the sender.
    ```{python}
    def broadcast(data, sender_socket, name):
*  
    * The function iterates over all client sockets, sending the message to each one except the sender. It also handles any exceptions and removes broken connections from the list of client sockets.
    ```{python}
    for client_socket in client_sockets:
        try:
          if client_socket == sender_socket:
            pass
          else:
            message = f"{name}: {data.decode('utf-8')}"
            client_socket.sendall(message.encode('utf-8'))
        except:
            client_sockets.remove(client_socket)
* 
    * The host and port for the server are defined, and a socket is created, bound to the host and port, and set to listen for incoming connections. An empty list client_sockets is initialized to keep track of connected clients.
     ```{python} 
     host = 'localhost'
     port = 5555
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     server_socket.bind((host, port))
     server_socket.listen(5)
     print(f"Server listening on {host}:{port}")
     client_sockets = []
*  
    * The server enters an infinite loop to accept incoming connections. When a client connects, the server accepts the connection, prints a message about the connection, adds the client's socket to the list of client sockets, and starts a new thread to handle the client's communication.
     ```{python} 
     while True:
         client_socket, client_address = server_socket.accept()
         print(f"Accepted connection from {client_address}")
         client_sockets.append(client_socket)
         client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
         client_handler.start()
* ## CLIENT SIDE CODE :
 ```{python} 
import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))
        except:
            break

def send_messages(sock):
    while True:
        message = input()
        sock.sendall(message.encode('utf-8'))
        if message.lower() == "quit" or message.lower() == "exit":
            break

def main():
    host = 'localhost'
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    welcome_msg = client_socket.recv(1024)
    print(welcome_msg.decode('utf-8'))

    name = input("Enter your name: ")
    client_socket.sendall(name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
    send_thread = threading.Thread(target=send_messages, args=(client_socket,), daemon=True)

    receive_thread.start()
    send_thread.start()

    send_thread.join()  # Wait for the sending thread to finish

    client_socket.close()

if __name__ == "__main__":
    main()


 ```
*  Similar to the server-side code, the socket and threading modules are imported for socket programming and multi-threading support.
    ```{python} 
    import socket
    import threading
* 
    * **receive_messages** function is defined to continuously receive and print messages from the server.
    ```{python} 
    def receive_messages(sock):
* 
    * he function continuously receives data from the server and prints it. If an exception occurs (e.g., connection closed), the loop breaks.
     ```{python} 
    while True:
        try:
          data = sock.recv(1024)
          print(data.decode('utf-8'))
        except:
          break
* 
    * **send_messages** function is defined to continuously take input from the user and send it to the server.
     ```{python}
    def send_messages(sock):
* 
    * The function continuously takes input from the user, sends it to the server, and checks if the user wants to quit or exit the chat.
    ```{python}
    while True:
        message = input()
        sock.sendall(message.encode('utf-8'))
        if message.lower() == "quit" or message.lower() == "exit":
          break
* 
    * main function is defined as the entry point of the client-side code. 
    ```{python}
    def main():
* 
    * The client creates a socket and connects to the server. It receives and prints the welcome message from the server, then prompts the user to enter their name and sends it to the server.
    ```{python}
      host = 'localhost'
      port = 5555
      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect((host, port))
      welcome_msg = client_socket.recv(1024)
      print(welcome_msg.decode('utf-8'))
      name = input("Enter your name: ")
      client_socket.sendall(name.encode('utf-8'))

*  
    * Two threads are created: one for receiving messages from the server (receive_thread) and one for sending messages to the server (send_thread). Both threads are started, and the main thread waits for the send_thread to finish before closing the client socket.
    ```{python}
      receive_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
      send_thread = threading.Thread(target=send_messages, args=(client_socket,), daemon=True)
      receive_thread.start()
      send_thread.start()
      send_thread.join() # Wait for the sending thread to finish
      client_socket.close()
*  
    * The main function is called when the script is executed as the main program. It initiates the client-side functionality.
    ```{python}
    if __name__ == "__main__":
       main()
# **Function Descriptions:**
  * ## Server-side:
       * #### handle_client:
          * Manages communication with a single connected client.
    * #### Sends a welcome message and receives the client's nickname.
    * #### Continuously receives messages from the client, broadcasts them to other clients, and handles exit requests.
    * #### Broadcast : 
       * Sends a message to all connected clients except the sender.
    * ## Client-side:
         * ### Receive_messages:
            * Runs in a separate thread to continuously receive and print messages sent by the server.
         * ### send_messages :
             * Runs in a separate thread to allow the user to input messages and send them to the server.
        * ### main :
             * Initializes the client socket, connects to the server, handles welcome messages, prompts for a nickname, and starts threads for receiving and sending messages
# RESULT _ OUTPUT : 
![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/1.BroadcasetMessage/Screenshot_20240121_164139.png)
![RESULT](https://github.com/ALFAJ01/dept.CST_CN_Pract/blob/master/1.BroadcasetMessage/2024-02-13%2016-41-36.mkv)
