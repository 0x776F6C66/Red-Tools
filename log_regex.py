#!/usr/bin/python3
#@author:wolf

#A friend thought of creating a script/tool that would help us parse log files to make getting specific info fast. This script is the outcome.
#I/we will continue to update and maintain the code as needs arises.

import os
import sys
import getopt

ip = False

def usage():
    print("usage: log_regex.py [options] file.")
    print("")
    print("Options")
    print("-------")
    print("-h              - print this and exit.")
    print("-i              - search for Ip addresses.")
    print("-f --file=file  - file to check.")
    exit()

def main():
    global ip
    global files

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:hi", ["help", "ip", "file="])
    except getopt.GetoptError as err:
        print(str(err))
        exit()

    for o, a in opts:
        if o in ['-h', '--help']:
            usage()
        elif o in ['-i', '--ip']:
            ip = True
        elif o in ["-f", "--file"]:
            files = a
            if not os.path.exists(files):
                print("File doesn't exist. Exiting !!\n")
                exit()

    if ip:
        print("\nIP addresses")
        print("------------")
        command = "grep -a -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' -o "+ files
        os.system(command)

if __name__ == "__main__":
    main()
    print("")
