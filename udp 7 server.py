import socket
import os
import subprocess
import time

# Time span (in seconds) to wait before opening the file
WAIT_TIME = 5

# Create UDP server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 8080))
print("UDP server listening for files...")

# Function to receive and save the video file
def receive_file(filename, end_marker):
    with open(filename, 'wb') as f:
        while True:
            data, client_address = udp_server.recvfrom(4096)
            if data == end_marker:
                break
            f.write(data)
    print(f"File '{filename}' received successfully.")

# Receive and play video file
video_filename = 'received_video.mp4'
receive_file(video_filename, b'EOF_VIDEO')

# Display filename and wait before opening the video file
print(f"Opening '{video_filename}' in {WAIT_TIME} seconds...")
time.sleep(WAIT_TIME)

# Automatically open the video file after the time span
try:
    if os.name == 'nt':  # For Windows
        os.startfile(video_filename)
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.run(['open', video_filename])  # For macOS
        # subprocess.run(['xdg-open', video_filename])  # For Linux
except Exception as e:
    print(f"Error while trying to open the video file: {e}")

# Optionally, receive the audio file if sent by the client
audio_filename = 'received_audio.mp3'
receive_file(audio_filename, b'EOF_AUDIO')

# Close the server socket
udp_server.close()
