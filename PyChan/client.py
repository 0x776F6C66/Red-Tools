#!/usr/bin/env python3

import socket
import sys
import select

#check if sufficient parameters are met.
if len(sys.argv) <3:
    print("Usage: client.py ip port username.")
    exit()

if __name__ == "__main__":
    #banner.
    print("\n\t===========================================================")
    print("\t                 PYCHAN client v1.0")
    print("\t              by P4rsz and W1nterFr3ak")
    print("\t   email:parsz@protonmail.com,WinterFreak@protonmail.com")
    print("\t============================================================\n")

#host and port.
host = sys.argv[1]
port = int(sys.argv[2])
user = str(sys.argv[3])

#socket object and connect to host.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))
server.send(user.encode())
data = server.recv(2048)
print(f"\t{data.decode()}")


#from where to receive input.
message_inputs = [sys.stdin, server]

#check for messages from whether it is the server or from you sending.
def main():
    while True:
        try:
            read_from, output_to, errors = select.select(message_inputs,[] ,[] )
            for x in read_from:
                #message from server.
                if x == server:
                    msg = server.recv(2048)
                    if msg:
                        print(msg.decode())
                    else:
                        print("Server disconnected.\n")
                        server.close()
                        exit()
                else:
                    msg = sys.stdin.readline()
                    server.send(msg.encode())
                    out = user + ":" + msg
                    sys.stdout.write(out)
                    sys.stdout.flush()
        except KeyboardInterrupt:
            server.close()
            exit()

if __name__ == '__main__':
    main()

server.close()
