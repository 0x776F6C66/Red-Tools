from threading import Thread
import socket
import sys

clients = []

#receive messages.
def Handler(conn, addr):
    while True:
        try:
            msg = conn.recv(1024)
            if msg:
                print(f"{addr}: {msg.decode()}")
                broadcast(conn, msg)
            else:
                conn.close()
                clients.remove(conn)
                print(f"{addr} disconnected.")
        except:
            continue

#send messages
def broadcast(conn, msg):

    for client in clients:
        print(client == conn)
        if conn != client:
            # if not client: blocking condition
            client.send(msg)

#accept connections and add the client to a list.
def accept_conn():
    while True:
        try:
            conn, addr = server.accept()
            # conn.send(b' Welcome to the server')
            print(f"[-] {addr} connected.")
            clients.append(conn)
            Thread(target=Handler, args=(conn, addr)).start()
        except KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    #banner.
    print("\n\t===========================================================")
    print("\t                 PYCHAN server v1.0")
    print("\t              by P4rsz and W1nterFr3ak")
    print("\t   email:parsz@protonmail.com,WinterFreak@protonmail.com")
    print("\t============================================================\n")

    #check if sufficient parameters are met.
    if len(sys.argv) <2:
        print("Usage: server.py ip port ")
        exit()

    #port and host
    host = str(sys.argv[1])
    port = int(sys.argv[2])

    #server object, binding.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((host, port))
    print(f"[-] Listening on {host} : {port}")
    server.listen(20)
    
    accept_conn()
