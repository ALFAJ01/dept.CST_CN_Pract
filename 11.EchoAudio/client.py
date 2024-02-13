import socket
import pickle
import struct
import pyshine as ps
import time

def send_audio(client_socket, audio_frame):
    # Sending the audio frame to the server
    try:
        a = pickle.dumps(audio_frame)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)
        print("Audio Sent ...")
    except Exception as e:
        print(f"Error sending audio: {e}")

def receive_audio(client_socket):
    # Receiving audio frame from the server
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

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = 'localhost'
port = 4982

socket_address = (host_ip, port)
client_socket.connect(socket_address)
print("CLIENT CONNECTED TO", socket_address)

try:
    # Get 5 seconds of audio from the client and send it to the server
    audio, context = ps.audioCapture(mode='get')
    ps.showPlot(context, 'CLIENT RECORDING AUDIO')
    
    start_time = time.time()
    while time.time() - start_time < 5:
        frame = audio.get()
        send_audio(client_socket, frame)

    # Receive the audio frames from the server and play them
    audio_frames = []
    while True:
        frame = receive_audio(client_socket)
        if frame is not None:
            audio_frames.append(frame)
            # You can play the audio frame using appropriate libraries here
except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()
