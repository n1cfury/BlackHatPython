 #!/ usr/bin/python
import sys, socket, threading

def banner():
	print "###  TCP Proxy p21  ###"

def usage():
	print " ./proxy.py [L_host] [L_port] [R_host] [R_port] [rcv_1st]"
	print "e.g. ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"

def srv_loop(L_host, L_port, R_host, R_port, rcv_1st):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server.bind((L_host,L_port))
	except:
		print "[!!] Failed to listed on %s:%d" % (L_host, L_port)
		print "[!!] Check for other listening sockets or correct permissions."
		sys.exit(0)
		print "[*] Listening on %s:%d % (L_host, L_port)"
		server.listen(5)
		while True: 
			c_socket, addr= server.accept()		#print local connection info
			print "[==>] Received incoming connection from %d:%s % (addr[0], addr[1]))"
			proxy_thread = threading.Thread(target=proxy_handler, args= (c_socket,R_host, R_port, rcv_1st_))
			proxy_thread.start()

def proxy_handler(c_socket, R_host, R_port, rcv_1st):			#connect to the remote host
	R_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	R_socket.connect((R_host, R_port))
	if rcv_1st:																#receive data from the remote end if necessary
		remove_buffer = rcv_from(R_socket)
		hexdump(R_buffer)
		R_buffer = response_handler(R_buffer)							#send it to our response proxy_handler
		if len(R_buffer):														#Sends data to the local client if available
			print "[<==] Sending %d bytes to L_host." % len(R_buffer)
			c_socket.send(R_buffer)
	while True:
		local_buffer = rcv_from(c_socket)									#read from local host
		if len(local_buffer):
			print "[==>] Received %d bytes from L_host." % len(local_buffer)
			hexdump(local_buffer)
			local_buffer = req_hadnler(local_buffer)							#send it to our request handler
			local_buffer = req_handler  										#Send it to our request handler
			R_socket.send(local_buffer)										#send off the data to the remote host
			print "[==>] Sent to remote."
			R_buffer = rcv_from(R_socket)								#receive back the response
			if len(R_buffer):
				print "[<==] Received %d bytes from remote." % len(R_buffer)
				hexdump(R_buffer)
				c_socket.send(R_buffer)									#send the response to the local socket
				print "[<==] Sent to L_host."
			if not len(local_buffer) or not len(R_buffer):						#if no more data on either side, close the connection
				c_socket.close()
				R_socket.close()
				print "[*] No more data.  Closing connections."
				break

def hexdump(src, length=16):			#hex dumping function from http://goo.gl/3LMHPj
	result = []
	digits = 4 if isinstance(src, unicode) else 2
	for i in xrange(o, len(src), length):
		s = src [i:i+length]
		hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
		text = b' '.join([x if 0x20 <= ord(x) < 0x7f else b'.' for x in s])
		result.append(b"%0*4X %-*s %s" (i, length*(digits + 1), hexa, text) )
	print b'\n'.join(result)

def rcv_from(connection):
	buffer = ""
	connection.settimeout(2)				#Two second timeout.  Adjust accordingly
	try:
		while True:							#keep reading into the buffer until there's no more data or it times out.
			data = connection.recv(4096)
			if not data:
				break
			buffer += data
	except:
	pass
	return buffer

def req_handler(buffer):   			#modify packets destined for the next remote host
	return buffer

def response_handler(buffer):			#modify packets destined for the local host
	return buffer

def main():
	if len(sys.argv[1:]) != 5:			#no fancy command-line parsing here
		usage()
		sys.exit(0)
	L_host = sys.argv[1]			#setup local listening parameters
	L_port = int(sys.argv[2])
	R_host = sys.argv[3]			#setup remote target
	R_port = sys.argv[4]
	rcv_1st = sys.argv[5]			#this tells our proxy to connect and receive data before sending to the remote host
	if "True" in rcv_1st
		rcv_1st = True
	else:
		rcv_1st = False
	srv_loop(L_host, L_port, R_host, R_port, rcv_1st)		#now spin up our listening socket

if __name__ = "__main__":
	main()