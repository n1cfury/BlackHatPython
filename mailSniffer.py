from scapy.all import *

def banner():
	print "[***]	Mail Sniffer p50	[***]"

def packet_callback(packet):
	print packet.show()

sniff(prn=packet_callback,count=1)