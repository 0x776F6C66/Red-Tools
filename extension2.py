#!/usr/bin/env python3
#@author:wolf

#The script checks which extensions a webpage allows.
#its a skeleton work and multithreading will be added later.

import sys
import requests
import getopt
import threading

# describe how the script works
def usage():
    print("Script checks what file extensions are allowed to be uploaded by a webpage.")
    print("Usage: extension2.py [options]")
    print("Options")
    print("-------")
    print("-h --help                - print this and exit.")
    print("-u --url=url             - the upload url.")
    print("-e --error=error         - the error message to check against. Make sure it's enclosed in double or single quotes.")
    print("-w --wordlist=wordlist   - wordlist containing file extensions to use.")
    print("""\nExample: ./extension.py -u http://google.com -e 'Extension not allowed' -w /seclists/Discovery/Web-Content/raft-large-extensions.txt\n""")
    exit()

#conduct the file extension validation.
def check(url, error, wordlist):
    try:
        for i in wordlist:
            name="index"+i
            filesz={'file': (name, '')}
            data = requests.post(url, files=filesz)
            if error not in data.text:
                print(f"Extension allowed: {i}")
    except:
        print("Error...exiting\n")
        exit()

#create a list from the wordlist
def create_small_lists(url, error, wordlist):

    lists = []
    lists2 = []
    files = open(wordlist, 'r')

    #read the file line by line, separate the words and store them in a list.
    for line in files:
        strip = line.strip()
        lists.append(strip)

    no_of_threads = 25 #number of threads to run. Ypu adjust speed of the script by changing this value.
    length_of_wordlist = len(wordlist) # get the length of the wordlist.
    words_in_thread = int(length_of_wordlist/no_of_threads)#get the number of words to be in each list to be handled by the 25               threads.

    #a loop that divides the wrdlist into equal chunks and stores in lists2.
    for x in range(0, length_of_wordlist, words_in_thread+1):
        x = lists[x:x+words_in_thread]
        lists2.append(x)

    for item in lists2:
        thread = threading.Thread(target=check, args=(url, error, item))
        thread.start()
        thread.join()

def main():
    global url
    global error
    global wordlist

    url = ""
    error = ""
    wordlist = ""

    #check if arguments are there
    if not len(sys.argv[1:]):
        usage()

    #get the arguments placed and their values. if error display errror and exit.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:e:w:h", ["help", "error=", "url=","wordlist="])
    except getopt.GetoptError as err:
        print(str(err))
        exit()

    for o,a in opts:
        if o in ["-h", "--help"]:
            usage()
        elif o in ["-u", "--url"]:
            url = a
        elif o in ["-e", "error"]:
            error = a
        elif o in ["-w", "--wordlist"]:
            wordlist = a

    #banner
    print("====================================")
    print("Extension checker")
    print("@author: Calvin Kimani (@wolf)")
    print("====================================")
    print(f"[*] Url:            {url}")
    print(f"[*] Error message:  {error}")
    print(f"[*] Wordlist:       {wordlist}")
    print("====================================\n")
    create_small_lists(url, error, wordlist)

if __name__ == "__main__":
    main()
