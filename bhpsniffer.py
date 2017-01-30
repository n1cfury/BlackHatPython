#add shebang here

#BlackHat Python Ch 3, p 37; bhpsniffer.py

import os, socket, sys #the OS module will enumerate OS's.  Added sys to allow arguments.

host = "Target IP"  #enter the target IP address.  consider adding an argument to enter any IP

#create a raw socket and bind it to the public interface
if os.name == "nt":
	socket_protocol = socket.IPPROTO_IP
else
	socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind = ((host, 0))

#We want the IP headers included in the cpature.
sniffer.setsockopt(socket.IPPROTO_IP, socket_IP_HDRINCL, 1)

#IF you're using windows you'll need to send an IOCTL for promiscuous mode

if os.name == "nt":
	sniffer.IOCTL(socket.SIO_RCVALL, socket.RCVALL_ON)
#read in a single packet
print sniffer.recvfrom(65565)
#if you're using windows, turn off promiscuous mode

if os.name == "nt":
	sniffer.IOCTL(socket.SIO_RCVALL, socket.RCVALL_OFF)