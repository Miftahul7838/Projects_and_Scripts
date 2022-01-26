import socket

# Local TCP server connection
target_host = "127.0.0.1"
target_port = 9998

# Uncomment the below 2 line for remote TCP client server connection
# target_host = "www.google.com"
# target_port = 80

# Create a TCP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host, target_port))

# Send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data 
response = client.recv(4096)

# Print the received data & close the client socket
print(response.decode())
client.close()