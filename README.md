# Nrewrite below documentation of server client program "1. Program Objective:

    The goal of this Python program is to create a simple chat application where multiple clients can connect to a server.
    Clients can send messages to the server, which then broadcasts the messages to all connected clients. The server also handles client disconnections gracefully.

2. Abstract Approach:

    To achieve the objective, the following approach is taken:

  Socket Module: The socket module is used for network communication between the server and clients.

  Threading Module: The threading module is utilized for managing multiple client connections concurrently.

  Functions:

     handle_client(client_socket, client_address): Handles individual client connections, receives and broadcasts messages.
     broadcast(data, sender_socket, name): Sends messages to all connected clients.
     receive_messages(sock): Function for a client to continuously receive messages from the server.
     send_messages(sock): Function for a client to continuously send messages to the server.
     main(): The main function for the client to establish a connection with the server and start sending and receiving message

3. Required Modules and Function Details:

   Server Side (server.py):

    Imports:
      socket: For network communication.
      threading: For handling multiple client connections concurrently.
     Functions:
      handle_client(client_socket, client_address): Handles a single client connection. Sends and receives messages.
      broadcast(data, sender_socket, name): Sends messages to all connected clients.
     Execution:
      Creates a server socket and binds it to a specified address.
      Listens for incoming connections.
      Accepts connections and handles them in separate threads.
      Maintains a list of connected client sockets.
      Broadcasts messages to all connected clients.
  Client Side (client.py):
    Similar to the server, it uses socket and threading modules.
     
    Functions:
      receive_messages(sock): Function for a client to continuously receive messages from the server.
      send_messages(sock): Function for a client to continuously send messages to the server.
      main(): The main function for the client to establish a connection with the server and start sending and receiving messages.
    Execution:
      Creates a client socket and connects to the server.
      Receives a welcome message from the server.
      Takes the client's name as input and sends it to the server.
      Spawns two threads: one for receiving messages and one for sending messages.
#CODE_EXPLAIN
  SERVER_SIDE:
      
    import socket
    import threading
      • Imports:
        ◦ The socket module provides a way to create sockets for network communication.
        ◦ The threading module is used for concurrent execution of functions or threads.
     
    def handle_client(client_socket, client_address):
      msg = """
              Welcome Md's Broadcasting Message Platform
                     o  o
                     <  __  >"""
      client_socket.sendall(msg.encode("utf-8"))
      • handle_client Function:
        ◦ This function is responsible for handling an individual client's connection.
        ◦ It starts by sending a welcome message to the client.
        ◦ The welcome message is a multiline string with a simple ASCII art representation.
     
      name = client_socket.recv(32).decode('utf-8')
      • Receiving Client Name:
        ◦ The server receives the client's name from the client. The recv method is used to receive data, and decode is used to convert the received bytes to a UTF-8 string.
  
     while True:
       data = client_socket.recv(1024)
       if not data:
         break
     • Message Reception Loop:
       ◦ The server enters a loop to continuously receive messages from the client.
       ◦ If the received data is empty, the loop breaks.
    
       if data.decode("utf-8").lower() == "quit" or data.decode("utf-8").lower() == "exit":
         data=f"{name} Exit From the Chat Server ".encode("utf-8")
         broadcast(data, client_socket, name)
         break
     • Handling Quit or Exit:
       ◦ If the received message from the client is "quit" or "exit," the server sends a farewell message, broadcasts it to all clients, and breaks out of the loop.
       
    message = f"{name}: {data.decode('utf-8')}"
       print(message)
       broadcast(data, client_socket, name)
     • Broadcasting the Message:
       ◦ The server constructs a message with the sender's name and the received message.
    ◦ It prints the message to the server's console.
    ◦ The broadcast function is called to send the message to all connected clients.
  
      print(f"Connection with {client_address} closed.")
      client_sockets.remove(client_socket)
      client_socket.close()
      • Closing Client Connection:
        ◦ Once the loop breaks, indicating the client has disconnected, the server prints a message about the closed connection.
        ◦ The client socket is removed from the list of connected sockets, and the socket is closed.
      
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
      • broadcast Function:
        ◦ This function sends a message (data) to all connected clients except the sender.
        ◦ It iterates through the list of connected sockets (client_sockets) and sends the message to each client.
        ◦ If there's an exception (possibly due to a broken connection), the broken connection is removed from the list.
      
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
     • Server Initialization:
       ◦ The server sets the host and port it will listen on.
       ◦ It creates a server socket using socket.AF_INET for IPv4 and socket.SOCK_STREAM for TCP.
       ◦ The server binds the socket to the specified host and port.
       ◦ The server listens for incoming connections with a maximum backlog of 5.
       ◦ The server then enters an infinite loop to accept connections from clients.
       ◦ For each accepted connection, a new thread is spawned (client_handler) to handle the client using the handle_client function.
    
   Note:
     • This code implements a basic chat server where clients can connect, send messages, and receive messages broadcasted to all connected clients.
     • Threading is used to handle multiple clients concurrently, allowing the server to serve multiple clients simultaneously.
     • The broadcast function ensures that messages from one client are sent to all other connected clients.
  CLIENT_SIDE:
    import socket
    import threading
      • Imports:
        ◦ The socket module provides a way to create sockets for network communication.
        ◦ The threading module is used for concurrent execution of functions or threads.

    def receive_messages(sock):
      while True:
        try:
          data = sock.recv(1024)
          if not data:
            break
          print(data.decode('utf-8'))
        except:
          break
      • receive_messages Function:
        ◦ This function continuously receives messages from the server (sock).
        ◦ The server sends messages in chunks of 1024 bytes, and the function decodes and prints them.
        ◦ If an exception occurs (possibly due to a broken connection), the loop breaks.

    def send_messages(sock):
      while True:
        message = input()
        sock.sendall(message.encode('utf-8'))
        if message.lower() == "quit" or message.lower() == "exit":
          break
      • send_messages Function:
        ◦ This function continuously sends messages to the server (sock).
        ◦ It takes input from the user and sends the message to the server after encoding it to bytes.
        ◦ If the user enters "quit" or "exit," the loop breaks.

    def main():
      host = 'localhost'
      port = 5555

      client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client_socket.connect((host, port))
      • main Function:
        ◦ The main function is the entry point for the client program.
        ◦ It sets the host and port to connect to.
        ◦ It creates a client socket using socket.AF_INET for IPv4 and socket.SOCK_STREAM for TCP.
        ◦ The client socket connects to the specified host and port.

      welcome_msg = client_socket.recv(1024)
      print(welcome_msg.decode('utf-8'))
      • Receiving Welcome Message:
        ◦ The client receives a welcome message from the server after connecting.
        ◦ The received message is decoded from bytes and printed.
      Sending Client Name:
       The client enters its name, and the name is sent to the server after encoding.

         receive_thread = threading.Thread(target=receive_messages, args=(client_socket,), daemon=True)
         send_thread = threading.Thread(target=send_messages, args=(client_socket,), daemon=True)

         receive_thread.start()
         send_thread.start()

         send_thread.join() # Wait for the sending thread to finish

         client_socket.close()
    Threading Setup:
     Two threads are created using the threading.Thread class, one for receiving messages (receive_thread) and one for sending messages (send_thread).
     Both threads are started using the start method.
     The send_thread.join() line ensures that the program waits for the sending thread to finish before closing the client socket.
     Finally, the client socket is closed.
     if __name__ == "__main__":
       main()
     Main Program Execution:
     The program checks if it is the main module and then calls the main function to start the client
" 
NBU_CST_Dept._CN_Practical By Mr. Soul Hacker

Instead of competing with others, we should focus on helping each other and uplifting one another. 
☀️ This collaborative approach creates a more positive and supportive environment where everyone can flourish. 🤝

# Remember, your biggest competition is yourself. 
Strive to be better than you were yesterday and constantly push your own boundaries. 
When you focus on your own growth, you'll naturally attract success and happiness. ✨

# So let's join hands and make the world a happier place, together!s 🫵🏻 
# Reach Me ..
 _____________________________
  https://alfaj01.github.io/

