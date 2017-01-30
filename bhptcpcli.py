 #!/ usr/bin/python

#Black Hat Python
#TCP Client
#page 10

/bin/bash: q: command not found
#blackhat python

import socket
target_host = "www.google.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the client

client.connect((target_host, target_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print response