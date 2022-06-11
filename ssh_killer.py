#!/usr/bin/env python
#@author:Calvin Kimani (@wolf)

                                                        ####IMPORTANT####
# /////    As of now, the script works like this.......It takes an ip address, adds it to the /etc/hosts.allow file. This makes the ssh server.  /////
# /////    accept ssh logins from the specified ip. The script then kills all ssh sessions and I mean ALL. Then you can login again. //////

#import necessary modules.
import os
#import re
import sys

#check if correct arguments are placed.
if len(sys.argv) != 2:
    print("MAKE SURE YOU PUT YOU IP CORRECTLY ELSE YOU'LL LOCK YOURSELF AND EVERYONE OUT.")
    print("./ssh_killer.py [your ip].")
    exit()

#banner
def banner():
    print("================================")
    print("| SSH Killer                   |")
    print("| ±uthor: C.Kimani (@wolf)     |")
    print("================================")

#ip to compare against.
ip = sys.argv[1]

#pattern to search for in regex for ip.
#pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

#main function
def main():
    #creat an ssh allow/deny file to allow ssh access to only a specific ip(s).
    try:
        os.system("sudo touch /etc/hosts.{allow,deny}")
        os.system(f"sudo echo 'sshd: {ip}' >> /etc/hosts.allow")
        os.system("[*] Echo succeded.")
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
    banner()
    main()
