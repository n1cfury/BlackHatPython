import socket, os, struct
from ctypes import *

host = "192.168.56.101" 	#consider adding a sys.argv

def banner():
	print "#Black Hat Python, Sniffer, IP Header Decoder p40"
	print "host to listen on (where you're doing the sniffing from)"

class IP(structure):			#our IP header
	_fields_ = 
	[
		("ihl", 			c_ubyte, 4),
		("version", 		c_ubyte, 4),
		("tos", 			c_ubyte),
		("len",				c_ushort),
		("id",				c_ushort),
		("offset",			c_ushort),
		("ttl",				c_ubyte),
		("protocol_num",	c_ubyte),
		("sum",				c_ushort),
		("src",				c_ulong),
		("dst",				c_ulong)
	]
def __new__(self, socket_buffer=None):
	return self.from_buffer_copy(socket_buffer)

def __init__(self, socket_buffer=None):
	#map protocol constants to their names
	self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}
	#human readable IP addresses
	self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
	self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))
	#human readable protocol
	try:
		self.protocol = self.protocol_map[self.protocol.protocol_num}]
	except:
		self.protocol = str(self.protocol_num)
if os.name == "nt":								# this should look familiar from the previous example
	socket_protocol = socket.IPPROTO_IP
else:
	socket_protocol = socket.IPPROTO_ICMP
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
if os.name =="nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	try:
		while True:
			raw_buffer = sniffer.recvfrom(65565)[0]
			ip_header = IP(raw_buffer[0:20])
			print "Protocol: %s %s -> %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)
		if os.name == "nt":
			sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)