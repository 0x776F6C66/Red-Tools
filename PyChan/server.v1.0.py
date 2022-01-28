from threading import Thread
import socket
import sys

#client handler
def Handler(client):
    while True:
        msg = client.recv(1024)
        if msg != b'quit':
            print(msg)
        else:
            client.close()
            break



#accept connections
def accept_conn():
    while True:
        conn, addr = server.accept()
        conn.send(b' Welcome to the server')
        print(f"[-] {addr} connected.")
        Thread(target=Handler, args=(conn, )).start()


if __name__ == "__main__":
    #banner.
    print("\n\t########  ###  ###  ########  ###  ###  ########  ###    ###")
    print("\t########  ###  ###  ########  ###  ###  ###  ###  ## #   ###")
    print("\t########  ###  ###  ##        ########  ###  ###  ### #  ###    server v1.0")
    print("\t########  ########  ##        ########  ########  ###  # ###    by P4rsz and W1nterFr3ak")
    print("\t####           ###  ########  ###  ###  ###  ###  ###   # ##    email:parsz@protonmail.com,WinterFreak@protonmail.com")
    print("\t####      ########  ########  ###  ###  ###  ###  ###    ###\n")

    #check if sufficient parameters are met.
    if len(sys.argv) <2:
        print("Usage: server.py ip port ")
        exit()

    #port and host
    host = str(sys.argv[1])
    port = int(sys.argv[2])

    #server object, binding.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    server.listen(10)
    print(f"[-] Listening on {host} : {port}")
    connect = Thread(target=accept_conn)
    connect.start()
