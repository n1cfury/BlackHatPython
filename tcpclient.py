 #!/ usr/bin/python
import socket, sys

usage = "bhptcpcli.py <target host> <port number>"
target_host = sys.argv[1]
target_port = sys.argv[2]

def banner():
	print "[***]	TCP Client p10		[***]"
	print "Functions were added to improve the tool"

def tcptool(target_host, target_port):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         	#Create a socket for the target host, port
	client.connect((target_host, target_port))                         	#Connect the client
	client.send("GET / HTTP/1.1\r\nHost: "+target_host+"\r\n\r\n")          	#Sends Data
	response = client.recv(4096)                                      	#Receives Data from socket connection
	print response													   	#

def main():
	if len(sys.argv) == 3:
		banner()
		tcptool(target_host, target_port)
	else:
		print usage

if __name__ == "__main__":
	main()