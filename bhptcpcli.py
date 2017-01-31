 #!/ usr/bin/python
#Black Hat Python: TCP Client, Pg 10
#TODO:  ADD SOME FUNCTIONS.  ALSO, TAKE A LOOK AT SOME OTHER CODE YOU'VE PUT TOGETHER. THIS MAY LOOK FAMILIAR<HINT>.

import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         #Create a socket for the target host, port
client.connect((target_host, target_port))                         #Connect the client
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")          #Sends Data
response = client.recv(4096)                                       #Receives Data from socket connection
print response
