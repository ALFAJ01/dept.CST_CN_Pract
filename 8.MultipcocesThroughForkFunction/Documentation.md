# **Question :** 
### Demostrate the simple Server - Client Program For handaling the multiple client through fork() method.
# **__Program Objectivity :__**
 * ####      Create a server-client application for handle multiple client by providing the simple server - client interface like day, date and time information upon user request through fork() function.
 * ### The server listens for client connections on a specific port and forks child processes to manage communication with each client.
 * #### The server listens for client connections and responds to commands to obtain the current day, date, or time.
 * #### The client allows users to input specific commands to retrieve the desired information and displays the received responses.
 # Abstract Approach:
 * #### The server uses sockets to listen for incoming client connections on a specific port.
 * #### Incoming connections trigger the server to fork a new child process to handle the client communication.
 * #### Each child process manages its assigned client independently, receiving commands, processing them, and sending responses.
 * #### This multiprocessing approach allows the server to serve multiple clients simultaneously, efficiently utilizing system resources. 
 * #### Commands like "quit" or "exit" terminate the connection.
# Algorithm For this Program :
*   ## Server :
     * #### Bind the server socket to the address and port.
     * #### Enter a loop:
         * Accept a new client connection.
         * Fork a child process to handle the client.
         * In the child process:
             * Send a welcome message to the client.
             * Continuously receive commands from the client.
                * Process the command:
                     * If "day", format and send the current day of the week.
                     * If "date", format and send the current date.
                     * If "time", format and send the current time.
                     * If "quit" or "exit", close the connection and remove the client.
                     * For invalid commands, send an error message.
             * Send the response to the client.
         * In the parent process:
             * Close the client socket to avoid resource leaks.
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
* ## os:
   * Enables process management (fork, exit).
* ## datetime:
   * Offers tools for working with dates and times.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
 ```{python} 
import socket
import os
from datetime import datetime

def send_response(client_socket, client_address):
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    print(f"<.......................PID: {os.getpid()} ...............>")

    wcmsg = "Welcome to the server"
    client_socket.sendall(wcmsg.encode("utf-8"))

    while True:
        try:
            command = client_socket.recv(1024).decode("utf-8")

            if command.lower() == "day":
                response = datetime.now().strftime("%A")
            elif command.lower() == "date":
                response = datetime.now().strftime("%y-%m-%d")
            elif command.lower() == "time":
                response = datetime.now().strftime("%H:%M:%S")
            elif command.lower() == "quit" or command.lower() == "exit":
                client_socket.close()
                break
            else:
                response = "You entered an invalid command"

            client_socket.sendall(response.encode("utf-8"))

        except Exception as e:
            print(f"Error handling client: {str(e)}")
            break

def handle_clients_in_process(server_socket):
    while True:  # Continuously accept clients
        client_socket, client_address = server_socket.accept()
        try:
            # Fork a child process to handle the client
            pid = os.fork()
            if pid == 0:  # Child process
                send_response(client_socket, client_address)
                os._exit(0)  # Terminate after handling the client
            else:  # Parent process
                client_socket.close()  # Close the socket in the parent
        except Exception as e:
            print(f"Error handling client: {str(e)}")

def bind_ser():
    host = "localhost"
    port = 9900

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_sock.bind((host, port))
        server_sock.listen(100)
        print(f"Server is listening on IP: {host} and Port: {port}")
        return server_sock  # Return the server socket
    except socket.error as msg:
        print("Server socket binding threw an error" + str(msg) + "\n" + "Retrying ....")
        return bind_ser()

def main():
    server_sock = bind_ser()

    while True:
        try:
            handle_clients_in_process(server_sock)
        except Exception as e:
            print(f"Error in main loop: {str(e)}")

if __name__ == "__main__":
    main()

 ```
 * 
    *  Import necessary modules: socket for socket programming, os for operating system related functions and for fork() , and datetime for getting current date and time.
    ```{python} 
    import socket
    import os
    from datetime import datetime
* 
    * Define a function send_response() to handle client requests. It prints the client's address and the process ID (PID) of the server.
    ```{python} 
    def send_response(client_socket, client_address):
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    print(f"<.......................PID: {os.getpid()} ...............>")

* 
    *    Send a welcome message to the client upon connection. Enter a loop to continuously receive commands from the client.
     ```{python}
    wcmsg = "Welcome to the server"
    client_socket.sendall(wcmsg.encode("utf-8"))

    while True:
        try:
            command = client_socket.recv(1024).decode("utf-8")

* 
     * Based on the command received from the client, prepare a response. If the command is "day", "date", or "time", send the current day, date, or time respectively. If the command is "quit" or "exit", close the client socket and break out of the loop. Otherwise, send a message indicating an invalid command.
     ```{python}
            if command.lower() == "day":
                response = datetime.now().strftime("%A")
            elif command.lower() == "date":
                response = datetime.now().strftime("%y-%m-%d")
            elif command.lower() == "time":
                response = datetime.now().strftime("%H:%M:%S")
            elif command.lower() == "quit" or command.lower() == "exit":
                client_socket.close()
                break
            else:
                response = "You entered an invalid command"

* 
    * Send the response to the client. Handle any exceptions that may occur during communication with the client.
    ```{python}
        client_socket.sendall(response.encode("utf-8"))

        except Exception as e:
            print(f"Error handling client: {str(e)}")
            break


* 
     *  Define a function handle_clients_in_process() to handle clients in a separate process. Continuously accept clients, fork a child process to handle each client, and close the socket in the parent process.
    ```{python}
    def handle_clients_in_process(server_socket):
         while True:  # Continuously accept clients
             client_socket, client_address = server_socket.accept()
             try:
                 # Fork a child process to handle the client
                 pid = os.fork()
                 if pid == 0:  # Child process
                     send_response(client_socket, client_address)
                     os._exit(0)  # Terminate after handling the client
                 else:  # Parent process
                     client_socket.close()  # Close the socket in the parent
             except Exception as e:
                 print(f"Error handling client: {str(e)}")

* 
     *  Define a function bind_ser() to bind the server socket to the host and port, and start listening for incoming connections. Retry if there's an error during binding.
    ```{python}
    def bind_ser():
        host = "localhost"
        port = 9900

        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         try:
             server_sock.bind((host, port))
             server_sock.listen(100)
             print(f"Server is listening on IP: {host} and Port: {port}")
             return server_sock  # Return the server socket
         except socket.error as msg:
             print("Server socket binding threw an error" + str(msg) + "\n" + "Retrying ....")
             return bind_ser()

* 
     *  The main function binds the server socket and enters a loop to handle clients in a separate process.
    ```{python}
    def main():
        server_sock = bind_ser()
    
        while True:
            try:
                handle_clients_in_process(server_sock)
            except Exception as e:
                print(f"Error in main loop: {str(e)}")

    if __name__ == "__main__":
        main()

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
     * **send_response:**
        * Handles communication with a single client, welcoming them, receiving and processing commands, sending responses, and handling errors.
     * **handle_clients_in_process:** 
         * Continuously accepts new client connections, forks child processes to handle them, and closes the sockets in the parent process to avoid resource leaks.
     * **bind_ser:**
         * Binds the server socket to the specified address and port, handling errors gracefully.
     * **main:**
         * Establishes the server socket, enters a loop to continuously handle clients using handle_clients_in_process, and gracefully handles exceptions.
  * ## Client-side:
     * **Main program loop:**
       * Continuously prompts the user for commands, sends them to the server, displays received responses, and terminates the connection upon receiving "quit" or "exit" from the server.
        
# RESULT _ OUTPUT : 
 ![RESULT](/home/mr./Downloads/NBU_MSC/!st_Sem/Practical_Paper/Computer_Network/BroadcastMessge/Screenshot_20240121_164139.png)
