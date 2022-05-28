#!/usr/bin/python3
import base64
import sys
import itertools

if not len(sys.argv[1:]):
    print("USAGE: <base64.py> <[-d]ecode/[-e]ncode> <shift> <string>")
    print("Encoding : base64.py -e 50 abcdefgh\n")
    print("Decoding : base64.py -d abcdefgh\n")
    exit()

option = sys.argv[1]

def encode(string_, shift):
    string = sys.argv[3]

    for x in range(1, shift+1):
        try:
            encoded = base64.b64encode(bytes(string_.encode()))
            string_ = encoded.decode()
            if x == shift:
                print(f"\nSHIFT {x}: {string_}")
        except:
            exit()

def decode(string_):
    for _ in itertools.count():
        try:
            decoded = base64.b64decode(string_)
            string_ = decoded.decode()
            print(f"\n{string_}")
        except:
            exit()


def main():
    print("\n=====================================================")
    print("\n Base64 shift Decoder and Encoder by wo1fbit")
    print("\n=====================================================")
    if option == "-e":
        shift = int(sys.argv[2])
        string = sys.argv[3]
        encode(string, shift)
    elif option == "-d":
        string = sys.argv[2]
        decode(string)
    else:
        print(f"\nThere is no option as {option}.\n")
        print("USAGE: <base64.py> <[-d]ecode/[-e]ncode> <shift> <string>")
        print("Example: base64.py -e 50 abcdefgh\n")
        print("Example: base64.py -d abcdefgh\n")
        exit()

if __name__ == "__main__":
    main()
