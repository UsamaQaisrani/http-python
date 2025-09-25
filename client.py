import socket 
from sockettype import *
import threading

class MyClient:
    def __init__(self, host="localhost", port=6842):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((self.host, self.port))
        self.running = True
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        print(f"Client listening on port: {self.port}")
        while self.running:
            try:
                chunk = self.sock.recv(1024)
                if not chunk:
                    self.stop()
                    break
                print(chunk.decode())
            except:
                self.stop()
                break

    def stop(self):
        print(f"Disconnecting from port: {self.port}")
        self.running = False
        self.sock.close()
    
    def send(self, message):
        print(f"Sending message on port: {self.port}")
        self.sock.sendall(message)


