## python sniffer. {'todos':'be a simple wireshark'}

import socket
import subprocess
from struct import unpack

class Socket():
	"""
	socket.AF_PACKET is used to send/receive raw packets
	socket.RAW is used to create a raw socket
	socket.ntohs(3) is used to "say" capture all packets even ethernet frames
	"""
	def __init__(self, iface):
		self.Socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
		self.Iface = iface
		self.Mode = "Normal"

	# put interface into promiscuous mode
	def Promisc(self):
		subprocess.run(["ifconfig", self.Iface, "promisc"])
		self.Mode = "promisc"

	# set the interface back into normal mode
	def Close(self):
		subprocess.run(["ifconfig", self.Iface, "-promisc"], capture_output=True)
		self.Mode = "Normal"

	# capture all packets
	def Capture(self):
		self.recvBuffer, self.addr = self.Socket.recvfrom(2048)
		return self.recvBuffer

	#decode the ethernet frame
	"""
	an ethernet frame consists of three parts where the first two parts are 6bytes in length while the other is 2bytes
	therefore the length of the ethernet frame is 14 bytes and these bytes are what we need from the buffer
	the first 6 bytes are the source MAC address, the next 6 bytes are the destination MAC address while the final
	2bytes show the Ether type(ip protocol used) from the tests done, the ether type shows 2048 which shows ipv4 was used
	"""
	def ethDecode(self, recvBuffer):
		self.ethFrame = unpack("!6s6sH", recvBuffer[0:14])
		self.sourceMAC = self.ethFrame[0].hex(":")
		self.destMAC = self.ethFrame[1].hex(":")
		self.etherType = self.ethFrame[2]
		return self.sourceMAC, self.destMAC, self.etherType
