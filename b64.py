#!/usr/bin/python3
import base64
import sys

if len(sys.argv) != 4:
    print("USAGE: <base64.py> <[-d]ecode/[-e]ncode> <shift> <string>")
    print("Example: base64.py -e 50 abcdefgh")
    exit()

option = sys.argv[1]
shift = int(sys.argv[2])
string = sys.argv[3]

def encode(string_):
    for x in range(1, shift+1):
        try:
            encoded = base64.b64encode(bytes(string_.encode()))
            string_ = encoded.decode()
            print(f"\nShift {x}: {string_}")
        except:
            exit()

def decode(string_):
    for x in range(1, shift+1):
        try:
            decoded = base64.b64decode(string_)
            string_ = decoded.decode()
            print(f"\nShift {x}: {string_}")
        except:
            exit()


def main():
    print("\n-- Base64 shift Decoder and Encoder by PAR$Z -- ")
    if option == "-e":
        encode(string)
    elif option == "-d":
        decode(string)
    else:
        print(f"\nThere is no option as {option}.\n")
        print("USAGE: <base64.py> <[-d]ecode/[-e]ncode> <shift> <string>")
        print("Example: base64.py -e 50 abcdefgh\n")
        exit()

if __name__ == "__main__":
    main()
