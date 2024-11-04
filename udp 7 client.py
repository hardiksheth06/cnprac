import socket

# Create UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)

# Send the video file in chunks
with open('video.mp4', 'rb') as f:
    chunk = f.read(4096)
    while chunk:
        udp_client.sendto(chunk, server_address)
        chunk = f.read(4096)

# Send end marker for the video file
udp_client.sendto(b'EOF_VIDEO', server_address)
print("Video file sent successfully.")

# Send the audio file in chunks (optional)
with open('audio.mp3', 'rb') as f:
    chunk = f.read(4096)
    while chunk:
        udp_client.sendto(chunk, server_address)
        chunk = f.read(4096)

# Send end marker for the audio file
udp_client.sendto(b'EOF_AUDIO', server_address)
print("Audio file sent successfully.")

# Close the client socket
udp_client.close()
