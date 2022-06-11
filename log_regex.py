#!/usr/bin/python3
#@author:calvinkimani@wolf

#A friend thought of creating a script/tool that would help us parse log files to make getting specific info fast. This script is the outcome.
#I/we will continue to update and maintain the code as needs arises.

#import the needed modules
import os
import sys
import getopt

#how to use
def usage():
    print("\nusage: log_regex.py [options] file.")
    print("")
    print("Options")
    print("-------")
    print("-h                  - print this and exit.")
    print("-i                  - search for Ip addresses.")
    print("-f --file=file      - file to check.")
    print("-s --ssh            - look for SSH related.")
    exit()

#banner
def banner():
    os.system("echo '=================================='")
    os.system("echo '|   Log Parser                   |'")
    os.system("echo '|   ±uthor: C.Kimani (@wolf)     |'")
    os.system("echo '=================================='")

#the main function
def main():
    #initialize items
    ip = False
    ssh = False 
    output = False
    files = ""
    out = ""

    if not len(sys.argv[1:]): # check if length of script is correct
        usage()

    #get the arguments passed to sys then create a dictionary (key is the option while its value is the argument passed) from the arguments.
    #If there is an error, print the error and exit.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:his", ["help", "ip", "ssh", "file="])
    except getopt.GetoptError as err:
        print(str(err))
        exit()

    #for each of the options, if the option is given by user, assign the arguments passed.
    for o, a in opts:
        if o in ['-h', '--help']:
            usage()
        elif o in ['-i', '--ip']:
            ip = True
        elif o in ['-s', '--ssh']:
            ssh = True
        elif o in ['-f', '--file']:
            files = a
            if not os.path.exists(files): #if the path is not correct, print error and exit.
                print("File doesn't exist. Exiting !!\n")
                exit()

    #checks if the options are set and executes the desired action.
    if ip:
        os.system("echo '\n'IP'\n'------------")
        command = "grep -a -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' -o " + files + " | sort -u"
        os.system(command)
    if ssh:
        command = f"grep -i sshd {files} | sort -u "
        os.system("echo '\n'SSH'\n'-----------")
        os.system(command)

#load the module/ initialize the script.
if __name__ == "__main__":
    banner()
    main()
    print("")