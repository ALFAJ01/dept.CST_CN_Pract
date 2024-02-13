# **Question :** 
### Write the Server - Client Program For Where Client Ping the another host through the server whether the host is rechable or not.
# **__Program Objectivity :__**
 * ####      Create a server-client application that allows users to remotely ping hosts and view the results.
 * #### The server accepts client connections, receives host names to ping, executes the ping command, and sends back the results.
 * #### The client provides a user interface for entering host names and displaying the received ping results.

 # Abstract Approach:
 * #### The server listens for client connections on a designated port.
 * #### Upon connection, the server welcomes the client and enters a loop:
     * Receives a host name from the client.
     * Executes the appropriate ping command based on the operating system.
     * Sends the ping results back to the client.
 * #### The client connects to the server, receives the welcome message, prompts for host names, sends them to the server, receives and displays the ping results, and allows termination with "quit" or "exit".
# Algorithm For this Program :
*   ## Server :
     * #### Create a socket and bind it to a specific port.
     * #### Enter a loop:
         * Accept a new client connection.
         * Welcome the client.
         * Enter a loop:
             * Receive a host name from the client.
             * If "quit" or "exit", close the connection and break the loop.
             * Execute the ping command for the host.
             * Send the ping results to the client.
*   ## Client:
     * #### Create a client socket and connect to the server.
     * #### Receive and display the welcome message.
     * #### Enter a loop:
         * Prompt the user for a host name to ping or to quit.
         * Send the host name to the server.
         * Receive and display the ping results.
         * If "quit" or "exit" entered, close the client socket and break the loop.
# **Required Modules and Libraries:**
* ## socket:
     * Provides functionalities for socket communication.
* ## subprocess: 
     * Enables executing external commands (ping).
* ## platform: 
     * Detects the operating system for command adjustments.
# CODE EXPAIN :
* **SERVER SIDE CODE :**
```{python}
import socket
import subprocess
import platform

# Determine the Ping Command According to the platform OS
def ping_host(t_host):
    sys_os = platform.system()
    if sys_os.lower() == "windows":
        command = ["ping", "-n", "3", t_host]
    else:
        command = ["ping", "-c", "3", t_host]
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as error:
        return f"Your entered command gives an {error.output}"

host = "localhost"
port = 9990

# Create a socket object from the socket module
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server_sock object with host and port
def bind_ser():
    try:
        server_sock.bind((host, port))
        server_sock.listen(1)
        print(f"Server is listening on IP: {host} and Port: {port}")
    except socket.error as msg:
        print("Server socket binding through an error" + str(msg) + "\n" + "Retrying ....")
        bind_ser()

def con_accept():
    clien, addr = server_sock.accept()
    print(f"Connection has been established with client IP {str(addr[0])} and port is {str(addr[1])}")
    send_response(clien)

def send_response(clien):
    wcmsg = "Welcome to the server"
    clien.sendall(wcmsg.encode("utf-8"))
    while True:
        host_for_ping = clien.recv(1024).decode("utf-8")
        if host_for_ping.lower() == "quit" or host_for_ping.lower() == "exit":
            clien.close()
            break
        ping_result = ping_host(host_for_ping)
        clien.sendall(ping_result.encode("utf-8"))

bind_ser()
while True:
    con_accept()

 ```
*  Import necessary modules: socket for socket programming, subprocess for running shell commands, and platform for determining the operating system.
*  Define a function **ping_host(t_host)** to ping the specified host (t_host). This function determines the appropriate ping command based on the operating system. It executes the command and returns the result.
    ```{python} 
    import socket
    import subprocess
    import platform

    # Determine the Ping Command According to the platform OS
    def ping_host(t_host):
        sys_os = platform.system()
        if sys_os.lower() == "windows":
            command = ["ping", "-n", "3", t_host]
        else:
            command = ["ping", "-c", "3", t_host]
        try:
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            return result
        except subprocess.CalledProcessError as error:
            return f"Your entered command gives an {error.output}"
    
* 
    * Define a function **bind_ser()** to bind the server socket to the host and port, and start listening for incoming connections. It retries if there's an error during binding.
    ```{python} 
    host = "localhost"
    port = 9990

    # Create a socket object from the socket module
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server_sock object with host and port
    def bind_ser():
        try:
            server_sock.bind((host, port))
            server_sock.listen(1)
            print(f"Server is listening on IP: {host} and Port: {port}")
        except socket.error as msg:
            print("Server socket binding through an error" + str(msg) + "\n" + "Retrying ....")
            bind_ser()

* 
    * Define a function **con_accept()** to accept incoming connections from clients. Upon connection, it sends a welcome message to the client and calls send_response(clien) to handle client requests.
    * Define a function **send_response(clien)** to handle client requests. It continuously receives the host address from the client. If the client wants to quit, it closes the connection. Otherwise, it pings the specified host and sends the ping result back to the client.
     ```{python} 
    def con_accept():
       clien, addr = server_sock.accept()
       print(f"Connection has been established with client IP {str(addr[0])} and port is {str(addr[1])}")
       send_response(clien)

    def send_response(clien):
     wcmsg = "Welcome to the server"
     clien.sendall(wcmsg.encode("utf-8"))
     while True:
         host_for_ping = clien.recv(1024).decode("utf-8")
         if host_for_ping.lower() == "quit" or host_for_ping.lower() == "exit":
              clien.close()
               break
         ping_result = ping_host(host_for_ping)
           clien.sendall(ping_result.encode("utf-8"))
    
* 
    * Bind the server socket and start accepting client connections. The server continues to run and accept connections indefinitely.
     ```{python}
    bind_ser()
    while True:
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
    command=input("Enter the the address which you wnant to ping or for Exit -> quit or exit: ")
    clien_sock.sendall(command.encode("utf-8"))
    response=clien_sock.recv(1024).decode("utf-8")
    print(response)
    if  command.lower() == "quit" or command.lower() == "exit":
        clien_sock.close()
        break
 ```
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
    * Enter a loop to continuously take input from the user. Send the host address to the server to ping it, and receive and print the ping result from the server. If the user enters "quit" or "exit", close the client socket and break out of the loop.
    ```{python} 
    while  True:
         command = input("Enter the address which you want to ping or for Exit -> quit or exit: ")
         clien_sock.sendall(command.encode("utf-8"))
         response = clien_sock.recv(1024).decode("utf-8")
         print(response)
         if  command.lower() == "quit" or command.lower() == "exit":
             clien_sock.close()
             break
# **Function Descriptions:**
  * ## Server-side:
       * **ping_host(t_host):**
          *  Executes the ping command for the specified host, captures the output, and handles potential errors.
       * **bind_ser():**
          * Binds the server socket to the specified address and port, handling errors gracefully.
       * **con_accept():**
          *  Accepts a new client connection and passes the client socket to send_response.
       * **send_response(clien):**
          * Welcomes the client, enters a loop to receive host names, executes pings, sends results, and handles termination.

* ## Client-side:
     * ### Main program loop:
        * Connects to the server, receives the welcome message, prompts the user for host names, sends them to the server, receives and displays the ping results, and terminates upon "quit" or "exit".

# RESULT _ OUTPUT : 
![RESULT](/home/mr./Downloads/NBU_MSC/!st_Sem/Practical_Paper/Computer_Network/BroadcastMessge/Screenshot_20240121_164139.png)