import re
import socket
import multiprocessing
import time

class MyServer:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def setup(self, host, port):
        self.sock.bind((host,port))
        self.sock.listen(1)
        print(f"Listening on port: {port}")

    def accept(self):
        while True:
            try:
                client, address = self.sock.accept()
                print(f"Got a connection from {address}")
                client.close()
            except KeyboardInterrupt:
                print("\nConnection Closed")
                self.stop()
                break

    def stop(self):
        self.sock.close()
    
    def send(self, message):
        self.sock.send(message)

class MyClient:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        print(f"Connecting to {port}")
        self.sock.connect((host, port))

    def receive(self):
        chunk = self.sock.recv(2048)
        print(chunk)
    
    def stop(self):
        self.sock.close()

def run_server(host, port):
    server = MyServer()
    server.setup(host, port)
    server.accept()


def run_client(host, port):
    time.sleep(1)  
    client = MyClient()
    client.connect(host, port)
    client.stop()

def main():
    port = 6842
    host = "localhost"

    server_process = multiprocessing.Process(target=run_server, args=(host, port))
    server_process.start()

    client_process = multiprocessing.Process(target=run_client, args=(host, port))
    client_process.start()

    client_process.join()
    server_process.terminate()  

def readDataInOctets(path):
    buffer = ""
    pattern = re.compile(r".*\n")
    with open(path, "r") as input_file:
        while True:
            chunk = input_file.read(8)
            if chunk == "":
                break
            buffer += chunk
            match = re.search(pattern, buffer)
            if match:
                buffer = re.sub(pattern, "", buffer, count = 1)
                yield match.group().strip()

if __name__ == "__main__":
    main()
