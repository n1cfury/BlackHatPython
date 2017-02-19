#!/usr/bin/env python
import os, socket, sys 		#Added sys module to allow arguments.

def banner():
	print "#######   BlackHat Python p 37; sniffer  #######"

host = "Target IP"  		#Host to listen on. Consider adding an argument to enter an IP

def smells(host):
	if os.name == "nt":						
		socket_protocol = socket.IPPROTO_IP
	else
		socket_protocol = socket.IPPROTO_ICMP
	sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
	sniffer.bind = ((host, 0))
	sniffer.setsockopt(socket.IPPROTO_IP, socket_IP_HDRINCL, 1)		#Include IP headers in the cpature.
	if os.name == "nt":												#IF you're using WinX you need to send an IOCTL for promiscuous mode
		sniffer.IOCTL(socket.SIO_RCVALL, socket.RCVALL_ON)
	#read in a single packet
	print sniffer.recvfrom(65565)									#if you're using WinX, turn off promiscuous mode
	if os.name == "nt":
		sniffer.IOCTL(socket.SIO_RCVALL, socket.RCVALL_OFF)

def main():
	banner()
	smells(host)

if __name__= "__main__":
	main()