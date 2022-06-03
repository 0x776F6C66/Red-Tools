#!/usr/bin/env python
#@author:Calvin Kimani (@wolf)

#import necessary modules.
import os
import re
import sys

#check if correct arguments are placed.
if len(sys.argv) != 2:
    print("MAKE SURE YOU PUT YOU IP CORRECTLY ELSE YOU'LL LOCK YOURSELF AND EVERYONE OUT.")
    print("./ssh_kill.py [your ip].")
    exit()

#ip to compare against.
ip = sys.argv[1]

#pattern to search for in regex for ip.
#pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

#main function
def main():
    #creata a ssh allow/deny file to allow ssh access to only a specific ip(s).
    try:
        os.system("sudo touch /etc/hosts.{allow,deny}")
        os.system(f"sudo echo 'sshd: {ip}' >> /etc/hosts.allow")
    except:
        print("Error creating /etc/hosts.{allow,deny}files.")
        exit()

    #kill all ssh sessions. After this login again.
    try:
        os.system("sudo pkill --signal HUP sshd")
    except:
        print("Error killing ssh sessions.")
        exit()

    #//////The part below is unfinished code to find users and kill them based on their IP addresses.It will be updated soon/////
    #/////Otherwise the part of the script above will do the trick. Run


    #while True:
        #run the who command and store in output..
        #output = os.popen("who").read()

        #split the output of who_command and stor them in a list.
        #lst = output.split(" ")
        #connected = []

        #creata a list of users in the machine.
        #for line in lst:
            #if pattern.search(line):
                #connected.append(pattern.search(line)[1])

        #check if connected users match ip addresse given.
        #for user in connected:
            #if user != ip:
                #print("Match")
            #elif user == ip:
                #print("Match")

if __name__ == "__main__":
    main()
