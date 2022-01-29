#!/usr/bin/env python3

from threading import Thread
import socket
import sys

clients = []
users = []
address = []

#receive messages.
def Handler(conn, addr, username, user, addre):
    while True:
        try:
            msg = conn.recv(1024)
            if msg:
                print(user + ":"+ msg.decode())
                msg1 = (username + (" :").encode() + msg)
                broadcast(msg1, conn)
            else:
                conn.close()
                clients.remove(conn)
                users.remove(user)
                address.remove(addre)
                print(f"{addr} : disconnected.")
        except:
            continue


def broadcast(message, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(message)
                print("message sent")
            except:
                print("Error sending message.")
                client.close()

#accept connections and add the client to a list.
def accept_conn():
    while True:
        try:
            conn, addr = server.accept()
            username = conn.recv(1024)
            user = username.decode()
            addre = addr[0]
            if addre in address:
                conn.send(b"There is already a connection....")
                conn.close()
            else:
                if user in users:
                    conn.send(b"Username taken. Choose another then try again......")
                    conn.close()
                else:
                    conn.send(b' Welcome to the server.......')
                    print(f"[-] {addr[0]} : {user} connected.")
                    clients.append(conn)
                    users.append(user)
                    address.append(addre)
                    for add in address:
                        print(add)
                    Thread(target=Handler, args=(conn, addr, username, user, addre)).start()
        except KeyboardInterrupt:
            for client in clients:
                client.close()
            server.close()
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
