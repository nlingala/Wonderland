import socket
import os

IP = "127.0.0.1"    # Change
SERVER_DATA_PATH = r'C:\Users\navne\Documents\3872_TA\robot_files' # Change path for your convenience

#*****************DO NOT CHANGE*********************
PORT = 3030
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
ERR = "error"
SEPARATOR = "<SEPARATOR>"
#***************************************************

def listen_for_director():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        msg = client.recv(SIZE).decode()
        if msg == "DISCONNECT":
            break
        filename, filesize = msg.split(SEPARATOR)
        filepath = os.path.join(SERVER_DATA_PATH, filename)
        f = open(filepath, "wb")
        bytes_read = client.recv(int(filesize))
        f.write(bytes_read)
        f.close()
    client.close()

def decode_file():

    # Test Code

    # Implement file decoding and playing on robot
    # *********** Your code goes here *********** #

    return

def main():
    listen_for_director()
    decode_file()

if __name__ == "__main__":
    main()
