import socket
import sys

IP = "127.0.0.1"
PORT = 3030
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1000000
ERR = "error"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        data = client.recv(SIZE).decode(FORMAT)
        cmd, msg = data.split("@", 1)

        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split(" ")
        if len(data) <= 2:   
            cmd = data[0]

            if cmd == "HELP":
                client.send(cmd.encode(FORMAT))
            elif cmd == "LOGOUT":
                client.send(cmd.encode(FORMAT))
                break
            elif cmd == "LIST":
                client.send(cmd.encode(FORMAT))
            elif cmd == "DELETE" and len(data) == 2:
                client.send(f"{cmd}@{data[1]}".encode(FORMAT))
            elif cmd == "UPLOAD" and len(data) == 2:
                path = data[1]
                try:
                    with open(f"{path}", "rb") as f:
                        text = f.read()
                        filename = path.split("/")[-1]
                        send_data = f"{cmd}@{filename}@{text}"
                        client.sendall(send_data.encode(FORMAT))
                except OSError as err:
                    print("OS error: {0}".format(err))
                    client.send(ERR.encode(FORMAT))
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    client.send(ERR.encode(FORMAT))
                    raise
            elif cmd == "SEND" and len(data) == 2:
                client.send(f"{cmd}@{data[1:]}".encode(FORMAT))
            else:
                client.send(ERR.encode(FORMAT))
        else:
            client.send(ERR.encode(FORMAT))

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
