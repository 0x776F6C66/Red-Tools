#!/usr/bin/python3
import base64
import sys

#check if correct number of arguments are there.
if len(sys.argv) != 4:
    print("USAGE: <base64.py> <[-d]ecode/[-e]ncode> <shift> <string>")
    print("Example: base64.py -e 50 abcdefgh")
    exit()

option = sys.argv[1]
shift = int(sys.argv[2])
string = sys.argv[3]

#function to encode the string.
def encode(string_):
    for x in range(1, shift+1):
        try:
            #encode string to bytes and to base64.
            encoded = base64.b64encode(bytes(string_.encode()))
            string_ = encoded.decode()
            print(f"Shift {x}: {string_}")
        except:
            exit()

#function to decode the string.
def decode(string_):
    for x in range(1, shift+1):
        try:
            #decode the string from base64.
            decoded = base64.b64decode(string_)
            #convert byte object to string.
            string_ = decoded.decode()
            print(f"\nShift {x}: {string_}")
        #catch errors.
        except:
            exit()

#main function.
def main():
    print("\n\t-- Base64 shift Decoder and Encoder by PAR$Z-- \n")
    if option == "-e":
        encode(string)
    elif option == "-d":
        decode(string)
    else:
        print("Check your arguments.\n")
        exit()

if __name__ == "__main__":
    main()
