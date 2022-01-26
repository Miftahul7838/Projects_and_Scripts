import socket
import sys
import threading
import subprocess
import gc

class NetCat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send(self):
        self.socket.connect((self.args.target, self.args.port))

        if self.buffer:
            self.socket.send(self.buffer)
        
        try:
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print(' User terminated.')
            self.socket.close()
            sys.exit()

    def __execute(self, cmd):
        cmd = cmd.strip()
        if not cmd:
            return
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = p.stdout.decode()
        return output

    def __handle(self, client_socket):
        if self.args.execute:
            output = self.__execute(self.args.execute)
            client_socket.send(output.encode())

        elif self.args.upload:
            file_buffer = b''
            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break

            with open(self.args.upload, 'wb') as f:
                f.write(file_buffer)
            message = f'Saved file {self.args.upload}'
            client_socket.send(message.encode())

        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    client_socket.send(b'BHP: #> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = self.__execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f'server killed {e}')
                    self.socket.close()
                    sys.exit()

    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print('[*] Netcat Server listening...')

        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(
                target=self.__handle, args=(client_socket,)
            )
            client_thread.start()

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()