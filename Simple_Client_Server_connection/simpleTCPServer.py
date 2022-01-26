import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def handle_client(client_socket):
    with client_socket as sock: # The "with" keyword automatically open and closes the client connection
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')

# Accecpts mutliple client connections using the threading module
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        # The target= is set to the function that is being used on the client and
        # arg= is set to the client that is accepted
        client_handler = threading.Thread(target=handle_client, args=(client,)) 
        client_handler.start()

if __name__ == '__main__':
    main()

    