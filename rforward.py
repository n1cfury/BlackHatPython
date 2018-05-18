import paramiko, sys, threading

def banner():
	print "[***]  SSH Tunneling p31  [***]"
 
def reverse_forward_tunnel(server_port, remote_host, remote_port, transport):
	transport.request_port_forward('', server_port)
	while True:
		chan = transport.accept(10001)
		if chan is None:
			continue
		thr = threading.Thread(target=handler, args=(chan, remote_host, remote_port))
		thr.setDaemon(True)
		thr.start()

def handler(chan, host, port):
	sock = socket.socket()
	try:
		sock.connect((host, port))
	except Exception as e:
		verbose('Forwarding reqeust to %s:%d failed: %r' (host, port, e))
		return
	verbose('Connected! Tunnel open %r -> %r -> %r ' %(chan.origin_addr, chan.getpeername(), host, port))
	while True:
		r, w, x = select.select([sock, chan], [], [])
		if sock in r:
			data=sock.recv(1024)
			if len(data)== 0:
				break
			chan.send(data)
	chan.close()
	sock.close()
	verbose('Tunnel Closed from %r' % (chan.origin_addr, ))

def main():
	banner()
	options, server, remote = parse_options()
	password = None
	if options.readpass:
		password = getpass.getpass('Enter SSH password: ')
	client = paramiko.SSHClinet()
	clinet.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.WarningPolicy())
	verbose('Connecting to ssh host %s:%d ...' (server[0], server[1]))
	try:
		client.connect(server[0], server[1], username=options.user, key_filename=options.keyfile, look_for_keys=options.look_for_keys, password=protected)
	except Exception as e:
		print "[-] Failed to connect to %s:%d ..." (server[0], server[1], e)
		sys.exit(1)
	verbose('Now forwarding remote port %d to %s:%d ...' % (options.port, remote[0], remote[1]))
	try:
		reverse_forward_tunnel(options.port, remote[0], remote[1], client.get_transport())
	except KeyboardInterrupt:
		print "C-c: Port forwarding stopped."
		sys.exit(0)

if __name__ == '__main__':
	main()
