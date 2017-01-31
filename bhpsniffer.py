#!/usr/bin/env python

#BlackHat Python Ch 3, p 37; bhpsniffer.py

import os, socket, sys 		#Added sys module to allow arguments.

host = "Target IP"  											#Consider adding an argument to enter any IP

if os.name == "nt":						
	socket_protocol = socket.IPPROTO_IP
else
	socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind = ((host, 0))

sniffer.setsockopt(socket.IPPROTO_IP, socket_IP_HDRINCL, 1)			#Include IP headers in the cpature.

if os.name == "nt":													#IF you're using windows you'll need to send an IOCTL for promiscuous mode
	sniffer.IOCTL(socket.SIO_RCVALL, socket.RCVALL_ON)
#read in a single packet
print sniffer.recvfrom(65565)										#if you're using windows, turn off promiscuous mode

if os.name == "nt":
	sniffer.IOCTL(socket.SIO_RCVALL, socket.RCVALL_OFF)




