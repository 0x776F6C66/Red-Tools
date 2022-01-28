import socket
import sys


if __name__ == "__main__":
    #check if sufficient parameters are met.
    if len(sys.argv) <2:
        print("Usage: client.py ip port ")
        exit()

    #banner.
    print("\n\t===========================================================")
    print("\t                 PYCHAN client v1.0")
    print("\t              by P4rsz and W1nterFr3ak")
    print("\t   email:parsz@protonmail.com,WinterFreak@protonmail.com")
    print("\t============================================================\n")

    #host and port.
    host = sys.argv[1]
    port = int(sys.argv[2])

    #socket object and connect to host.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    while True:
        data = client.recv(1024)
        print(f"\t{data.decode()}")
        if data:
            print(data)
        msg = bytes(input(f"{host}@msg> "), 'utf-8')
        if msg != b'quit':
            client.send(msg)
        else:
            client.close()
            exit()

        
