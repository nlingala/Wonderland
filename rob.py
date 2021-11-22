# File: rob.py
# ECE 3872 Spring 2022 Wonderland Project
# Author: Navneet Lingala
# Robot Program for "Director-Robot" Connection
# ONLY modify lines that have been highlighted as MODIFIABLE

import socket
import os

IP = "127.0.0.1"        # MODIFIABLE: Change server IP as needed. Should be hardcoded already

SERVER_DATA_PATH = r'C:\Users\navne\Documents\3872_TA\robot_files'          # MODIFIABLE: Change robot data path as needed.

PORT = 3030
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
ERR = "error"
SEPARATOR = "<SEPARATOR>"

## Function that accepts incomming files.
 # Files are stored in the path stated above.
 ##
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


# runs fils listener
# Other computation can be coded here
def main():
    listen_for_director()
    decode_file()

    # *********** Your code goes here *********** #


# Script to call main function
if __name__ == "__main__":
    main()
