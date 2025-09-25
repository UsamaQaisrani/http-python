import re
from client import MyClient
from server import MyServer

def main():
    server = MyServer()
    client = MyClient()

    for line in readDataInOctets("message.txt"):
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
