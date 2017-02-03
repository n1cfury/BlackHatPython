#!/usr/bin/env python
import threading, paramiko, subprocess

usage = "./bh_sshcmd.py <hostname> <user> <password> <command>"
host = sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]
command = sys.argv[4]

def banner():
    print "############   n1cFury SSH Client  #################"			#Black Hat Python; SSH w/ Paramiko (p 26)

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	#client.load_host_keys('/home/justin/.ssh/known_hosts')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username= user, password= passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024) 										#reads the first 1024 bytes from the target host
	return

def main():
	banner()
	if sys.argv == 5:
		ssh_command(ip, user, passwd, command)
	else:
		print usage

if __name__ == "__main__":
	main()
