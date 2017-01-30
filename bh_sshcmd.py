#!/usr/bin/env python

#Black Hat Python; SSH w/ Paramiko (p 26)

import threading, paramiko, subprocess


def banner():
    print "############   n1cFury- NetCat tool   #################"
    print "############  courtesy of Black Hat Python  ###########"
    print ""

def usage():
	print "./bh_sshcmd.py <hostname> <user> <password> <command>"
	print ""
def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	#client.load_host_keys('/home/justin/.ssh/known_hosts')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username= user, password= passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024) 	#read banner
	return
ssh_command('192.168.1.59', 'justin', 'lovesthepython','id')

def main():
	if sys.argv == 5:
		banner()
		ssh_command(ip, user, passwd, command)
	else:
		print usage


if __name__ == "__main__":
	main()
