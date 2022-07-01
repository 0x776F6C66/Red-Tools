#!/usr/bin/env python3

import socket
import os
import sys

def banner():
	os.system("clear")
	print("=== PyCAT By 0x776F6C66 @wolf ===")

if len(sys.argv) != 2:
	banner()
	print("Usage: ./server.py port")
	print("Example: ./server.py 1234")
	print("By default the script listens on all interfaces")
	exit()

ip = "0.0.0.0" # listen on all interfaces //CHANGE THIS IF NEEDED
port =  int(sys.argv[1])#

def handler():
	tries = 0
	try:
		banner()

		# create tcp ipv4 socket, bind it to the ip and port, listen and accept connections
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse the port if needed
		server.bind((ip, port))
		server.listen(1)
		print(f"[*] Listening on {ip} port {port}")
		conn, addr = server.accept()
		print(f"[*] {addr[0]} connected..")
	
		while True:
			command = input("0x776F6C66: ") #prompt

			# catch empty commands and commands meant for the local machine
			if command == "":
				continue
			elif command.lower() == "clear":
				os.system("clear")
				banner()
				continue

			# send the commands, recv output and display it
			if command.startswith("cd"):
				if tries == 0:
					print("\nFrom @0x776F6C66: Apparently cd breaks the program for some umknown reasons....")
					print("os.chdir() on the client program breaks it, other methods have been researched with no fruits..")
					print("Try not changing into any directories ;0 \n")
					tries = 1
				continue

			conn.send(command.encode())

			if command.lower() == "exit": # terminate the connection when the user wishes
				return "Connection terminated.. :0"

			result = conn.recv(1024)
			
			if result.decode() == "": # check of the client has terminated connection
				return "Connection terminated.. :0"

			print(result.decode().strip("\n"))
	
	except KeyboardInterrupt:
		exit()
	except:
		return ""
	

def main():
	while True:
		x = handler()
		print("\n"+x)
		option = input("Restart (y/n)? ")
		if option.lower() == "y":
			continue
		elif option.lower() == "n":
			break


if __name__ == "__main__":
	main()
