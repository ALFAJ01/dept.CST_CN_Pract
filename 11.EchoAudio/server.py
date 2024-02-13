import socket
import pickle
import struct
import pyshine as ps
import time

def receive_audio(client_socket):
    # Receiving audio frame from the client
    data = b""
    payload_size = struct.calcsize("Q")

    try:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            if not packet:
                break
            data += packet
            print("Data Received ... ")

        if len(data) >= payload_size:
            packed_msg_size = data[:payload_size]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            while len(data) < msg_size:
                data += client_socket.recv(4 * 1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            print("Data Received ... ")

            return frame
        else:
            print("Insufficient data received.")
            return None

    except Exception as e:
        print(f"Error receiving audio: {e}")
        return None

def send_audio(client_socket, audio_frame):
    # Sending the audio frame to the client
    try:
        a = pickle.dumps(audio_frame)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)
        print("Audio Sent ...")
    except Exception as e:
        print(f"Error sending audio: {e}")

# Socket Create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = 'localhost'
port = 4982
backlog = 5
socket_address = (host_ip, port)
print('STARTING SERVER AT', socket_address, '...')
server_socket.bind(socket_address)
server_socket.listen(backlog)

while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    
    if client_socket:
        try:
            # Receive 5 seconds of audio from the client
            audio_frames = []
            start_time = time.time()
            while time.time() - start_time < 5:
                frame = receive_audio(client_socket)
                if frame is not None:
                    audio_frames.append(frame)

            # Send the received audio frames back to the client
            for frame in audio_frames:
                send_audio(client_socket, frame)

        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
    else:
       break
