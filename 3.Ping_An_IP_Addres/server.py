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
