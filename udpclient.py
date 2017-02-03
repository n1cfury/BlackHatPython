 #!/ usr/bin/python
import socket, sys

usage = "updcli.py target_host target_port"
target_host = sys.argv[1]
target_port = sys.argv[2]

def banner():
	print "##### UDP Client  #######"					#Blackhat Python UDP Client, pg 11
	print ""

def udpclient(target_host, target_port):
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client.sendto("AAABBBCCC", (target_host, target_port))
	data, addr = client.recvfrom(4096)
	print data

def main():
	if sys.argv == 3:
		banner()
		udpclient(target_host, target_port)
	else: 
		print usage

if __name__ = "__main__":
	main()
