
# Documentation for Date and Time Server with Multiprocessing - Client Program
# Program Objectives:

Create a server-client application that provides date and time information upon user request.
Enhance the server functionality to utilize multiple processes for handling client connections concurrently, improving performance and scalability.
The server listens for client connections on a specific port and forks child processes to manage communication with each client.
The client remains unchanged, sending commands (day, date, time) to the server and receiving responses.
# Abstract Approach:

The server uses sockets to listen for client connections on a specific port.
Incoming connections trigger the server to fork a new child process to handle the client communication.
Each child process manages its assigned client independently, receiving commands, processing them, and sending responses.
This multiprocessing approach allows the server to serve multiple clients simultaneously, efficiently utilizing system resources.
# Required Modules and Libraries:

socket: Provides functionalities for socket communication.
os: Enables process management (fork, exit).
datetime: Offers tools for working with dates and times.
# Function Descriptions:

Server-side:

send_response: Handles communication with a single client, welcoming them, receiving and processing commands, sending responses, and handling errors.
handle_clients_in_process: Continuously accepts new client connections, forks child processes to handle them, and closes the sockets in the parent process to avoid resource leaks.
bind_ser: Binds the server socket to the specified address and port, handling errors gracefully.
main: Establishes the server socket, enters a loop to continuously handle clients using handle_clients_in_process, and gracefully handles exceptions.
Client-side:

Main program loop: Connects to the server, receives the welcome message, prompts the user for commands, sends them to the server, displays received responses, and terminates the connection upon receiving "quit" or "exit" from the server.
# Program Algorithm:
#  __** Server:**__

Bind the server socket to the address and port.
Enter a loop:
Accept a new client connection.
Fork a child process to handle the client.
In the child process:
Send a welcome message to the client.
Continuously receive commands from the client.
Process the command:
If "day", format and send the current day of the week.
If "date", format and send the current date.
If "time", format and send the current time.
If "quit" or "exit", close the connection and terminate the child process.
For invalid commands, send an error message.
Send the response to the client.
In the parent process:
Close the client socket to avoid resource leaks.
Maintain the main loop to manage potential errors.
#    Client:

Create a client socket and connect to the server.
Receive and display the welcome message.
Enter a loop:
Prompt the user for a command (day, date, time, or quit/exit).
Send the command to the server.
Receive and display the server's response.
Check if the command was "quit" or "exit".
If user wants to exit, close the client socket and terminate the program.
