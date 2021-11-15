import os
import socket
import threading
import time

# , "127.0.0.1": "R02", "127.0.0.1": "R03"

# ROBOT = {"127.0.0.1": "R01"}

IP = "127.0.0.1"
SIZE = 1024
FORMAT = "utf-8"
PORT = 3030
ADDR = (IP, PORT)
NUM_R = 3
SERVER_DATA_PATH = r'C:\Users\navne\Documents\3872_TA\files'
SEPARATOR = "<SEPARATOR>"

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


def buffer_enumerate_files(name, buffer):
    file = []
    for e in buffer[name]:
        file.append(e[0])
    return file

def buffer_enumerate_times(name, buffer):
    time_after_cue = []
    for e in buffer[name]:
        if len(time_after_cue) == 0:
            time_after_cue.append(e[1])
        else:
            time_after_cue.append(e[1]-time_after_cue[-1])
    return time_after_cue

#returns ms since the epoch
def millis():
        return time.time() * 1000

def switchTheThing(howlong):
    start = millis()
    while ( (start + howlong) > millis() ):
        pass

def handle_client(conn, addr, file_list, time_list):
    print(f"[NEW CONNECTION] {addr} connected.")
    # conn.send("Welcome to the Director Server.".encode(FORMAT))
    while True: 
        count = threading.active_count() - 1
        time.sleep(3)
        if count == 1:  
            # print("started")
            # start = time.perf_counter()
            for i in range(len(file_list)):
                switchTheThing(time_list[i])
                filepath = os.path.join(SERVER_DATA_PATH, file_list[i])
                filesize = os.path.getsize(filepath)
                conn.send(f"{file_list[i]}{SEPARATOR}{filesize}".encode())
                with open(filepath, "rb") as f:
                    while True:
                        # read the bytes from the file
                        bytes_read = f.read(filesize)
                        if not bytes_read:
                            # file transmitting is done
                            f.close()
                            break
                        # we use sendall to assure transimission in busy networks
                        conn.sendall(bytes_read)

                # finish = time.perf_counter()
                # print(f'finished in {round(finish-start,3)} seconds(s)')
            break
    print(f"[DISCONNECTED] {addr} disconnected")
    conn.send("DISCONNECT".encode())
    conn.close()

# def robot_connection(addr, buffer):
#     return (buffer_enumerate_files(ROBOT[addr], buffer), buffer_enumerate_times(ROBOT[addr], buffer))

def main():
    print("[STARTING] Server is starting") 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}.")
    robot_addr = []
    num = input("Number of Robots: ")
    for i in range(int(num)):
        rob_ip = input("Robot IP: ")
        robot_addr.append(rob_ip)
    print()
    buffer = {}
    buffer_load(buffer)
    while True:
        conn, addr = server.accept()
        file_list = []
        time_list = []
        # file_list, time_list = robot_connection(addr[0], buffer)
        for ind, i in enumerate(robot_addr):
            if addr[0] == i:
                file_list = buffer_enumerate_files("R0" + str(ind + 1), buffer)
                time_list = buffer_enumerate_times("R0" + str(ind + 1), buffer)
        
        thread = threading.Thread(target=handle_client, args=(conn, addr, file_list, time_list))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        # count = threading.active_count() - 1
        # if count == NUM_R: 
        #     start = time.perf_counter()
        #     while True:
        #         count = threading.active_count() - 1
        #         if count == 0:
        #             finish = time.perf_counter()
        #             print(f'finished in {round(finish-start,3)} seconds(s)')
        #             break


if __name__ == "__main__":
    main()
