import re
from listeners.client.client import MyClient
from listeners.server.server import MyServer
import time

def main():
    server = MyServer()
    client = MyClient()

    for line in readDataInOctets("message.txt"):
        time.sleep(0.01)
        client.send(line.encode())

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
