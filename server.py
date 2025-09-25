import socket
import threading

class MyServer:
    def __init__(self, host="localhost", port=6842):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"Server listening on port: {self.port}")

        self.conn = None
        self.addr = None
        self.running = True

        threading.Thread(target=self.accept, daemon=True).start()


    def accept(self):
        self.conn, self.addr = self.sock.accept()
        print(f"Client connected: {self.addr}")
        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        while self.running:
            try:
                chunk = self.conn.recv(1024)
                print(chunk.decode())
                if not chunk:
                    self.stop()
                    break
            except:
                self.stop()
                break

    def stop(self):
        print(f"Server disconnecting from port: {self.port}")
        self.running = False
        if self.conn:
            self.conn.close()
        self.sock.close()
    
    def send(self, message):
        if self.conn:
            self.conn.sendall(message)

