#### day one...............

# Network Sniffing.
This is part of the [15 days of hacking challenge](https://github.com/P4rsz/15-days-of-Hacking)
In collaboration with [Fr334aks-TTW](https://github.com/fr334aks-TTW/15-days-of-hacking).

Aim of this project is to understand how data is sent, received and processed within networks and later build a sniffer tool based on the knowledge.
The main motivation behind the study is because I am naturally curious and I love to learn. The other reason is that it's an exciting venture on itself. Have fun and use the work here for good purposes.

# Network Interface cards(NIC)
![Network Interface Card](https://www.tutorialspoint.com/assets/questions/media/17618/chip.jpg) ![External NIC](https://www.tutorialspoint.com/assets/questions/media/17618/network.jpg)

Computers are connected to networks via hardware components known as [Network Interface Cards](https://www.tutorialspoint.com/what-is-network-interface-card-nic). Each NIC has a hardware address (the one we're calling the MAC address). This address is literally "burned" into the machine so it is permanent. When a computer is connected to a router, it's given an ip address to identify it from other computers in the network. Now our host has two addresses, the IP address and it's MAC address.

# How Data is exchanged in a network.

When you send data to another computer, it is in form of packets. The packet has an IP source and destination so it knows where it is going to and from where it is coming from.

# Packets and frames.
## Packet

A [Packet](https://en.wikipedia.org/wiki/Network_packet) is a small amount of data carried by a [packet-switched-network](https://en.wikipedia.org/wiki/Packet_switching). A packet contains control information and user data. The control information contains where all details about the packet are. Think of it as the content page of a book. It contains information such as destination address of the
packet, the sender, the protocol, the length of the packet e.t.c while the user data is the message or actual content of the packet.The main purpose of a packet is actually to append a network address to your data. 

![Packet Structure](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/IPv4_Packet-en.svg/1280px-IPv4_Packet-en.svg.png)

## Frames 
[Frames](https://en.wikipedia.org/wiki/Frame_(networking)) are used to help us identify the device we want to communicate with on the current circuit. Frames contain the MAC address which is important in this project. It helps to identify using the decice's [MAC address](https://en.wikipedia.org/wiki/MAC_address)(Media Access Control Address).

![Frame Structure.](https://upload.wikimedia.org/wikipedia/commons/1/13/Ethernet_Type_II_Frame_format.svg)

**Note**: There are two addresses we've talked about. The network address which is on the packet and the MAC address which is on the frame.

#### day two.................
# Address Resolution Protocol(ARP)
![TCP/IP OSI model](https://www.guru99.com/images/1/102219_1135_TCPIPvsOSIM1.png)
According to the [tcp/ip](https://www.javatpoint.com/computer-network-tcp-ip-model) and [OSI model](https://www.forcepoint.com/cyber-edu/osi-model) when a packet  reaches it's intended network, it interacts with the physical layer first before interacting with any other layers. We now go back to our packet. It has a network address which assists in knowing which network and host it is being to sent to but it has to interact first with the physical layer before talking with the network layer where the network adress is better understood. So now because we're dealing with the physical layer, we need "physical stuff". The router of the receiving network has got the packet but the router is part of the physical layer. How will it know where to send the packet because the packet has no physical address it can understand? This is where [ARP](https://www.techtarget.com/searchnetworking/definition/Address-Resolution-Protocol-ARP) comes in.

For the router to know which physical device it's supposed to send the packet, it calls for the assistance of ARP. Address Resolution Protocol esentially works by converting the ip address of the packet to it's corresponding MAC address. So the ARP broadcasts an ARP packet to every computer on the network....

**ARP program:** Yo sup guys. How you doing....Pleasantries aside,I have a packet with the IP address of x.x.x.x. If you're x.x.x.x, send me your MAC address.My
MAC address is this one.

The host with the IP address x.x.x.x sends it's MAC address to the ARP program which updates it's ARP cache. This is just a table which maintains a list of IP addresses with their corresponding MAC addresses. ARP cache size is limited and is periodically cleansed of all entries to free up space. Addresses tend to stay in the cache for only a few minutes so the need to call out every few minutes.

Now the router has a physical address to send the packet but how will it know which computer has a specific address. It will do this in a "hit and luck" fashion. The packet will be put in a frame (Yeah this is where frames come in). The frame has information on it which includes the MAC addresss of the receiving computer. The frame is sent out to every computer on the network (the hit) and the computer which is meant to receive will get it's data (the luck). As data flows in the network, every NIC on the network will "hear" the frames on the wire. When a frame arrives, it is copied into the memory inside the NIC, which checks the destination address in the header; if the address matches it's MAC address, the frame is processed accordingly and if it doesn't match it is discarded quielty by the computer.

#### to be continued tommorrow day three of the challenge............
