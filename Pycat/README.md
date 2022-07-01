# PyCAT

~~~
 useful where tools like netcat e.t.c are not installed on target system
 corrections and upgrades highly encourged
~~~

# IMPORTANT:

Traversing the directory structure of any system is important. However 'cd' command doesn't work in the program. Using os.chdir() in the client program to change directories breaks the client program therefore is not included. I've researched on ways to be able to traverse the target system but everything that would have been an altenative seems not to work. If you know how to fix the problem, i'd very much appreciate if you shared the solution.... thsnks

Email: shellbash0@gmail.com

⭐ twitter.com/0x776F6C66
---

# INBUILT COMMANDS (You can change them in the source code)
### Most if not all of the commands you'll execute depend on the type of operating system the client program is deployed
---
## 1. get - download files
~~~
get /path/to/file
~~~
