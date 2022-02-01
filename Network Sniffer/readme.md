# Network Sniffing.
[This is part of the 15 days of hacking challenge.](https://github.com/P4rsz/15-days-of-Hacking)
[In collaboration with fr334aks-TTW.](https://github.com/fr334aks-TTW/15-days-of-hacking)

The aim of this project is to create a sniffer tool built on the understanding of how data is sent, received and processed within networks.
I decided to work on the project because i am naturally curious on learning what is going on behind the scenes. The other reasons is that it's an exciting
venture on itself. Have fun and use the work here for good purposes.

# Packets and frames.
## Packet
Before we start, we need to know how data is sent across a network. A [Packet](https://en.wikipedia.org/wiki/Network_packet) is a small amount of data carried by a
[packet-switched-network](https://en.wikipedia.org/wiki/Packet_switching). A packet contains control information and user data. The control information is the
part of the packet where all details about the packet are. Think of it as the content page of a book. It contains information such as destination address of the
packet, the sender, the protocol, the length of the packet e.t.c while the user data is the message or actual content of the packet.The main purpose of a packet is
actually to append a network address to your data. 

![Packet Structure](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/IPv4_Packet-en.svg/1280px-IPv4_Packet-en.svg.png)

## Frames. 
[Frames](https://en.wikipedia.org/wiki/Frame_(networking)) are used to help us identify the device we want to communicate with on the current circuit. Frames contain the link address which is important in this project
plus other stuff.

![Frame Structure.](https://upload.wikimedia.org/wikipedia/commons/1/13/Ethernet_Type_II_Frame_format.svg)

Note: There are two addresses we've talked about. THe network address which is on a packet and the link address which is on the frame. The network address is the
      final destination while the link address is like say the physical address of the machine we're communicating with.
      
 ## How Data is exchanged in a network.
 To be continued on day two........
