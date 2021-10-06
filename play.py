import os
import socket
import threading

SERVER_DATA_PATH = r'C:\Users\navne\Documents\3872_TA\files'

def buffer_load(buf):
    files = os.listdir(SERVER_DATA_PATH)
    for f in files:
        rob, cue_time= f.split("_")
        cue_time = cue_time.split(".")[0]
        cue_time = int(cue_time)
        tup = (f, cue_time)
        if rob in buf:
            if not isinstance(buf[rob], list):
                buf[rob] = [buf[rob]]
            buf[rob].append(tup)
            buf[rob].sort(key=lambda tup: tup[1])
        else:
            buf[rob] = tup


def main():
    buffer = {}
    buffer_load(buffer)
    print(buffer)

if __name__ == "__main__":
    main()
