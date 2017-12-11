#ssh -i "key_pair.pem" ubuntu@ec2-35-164-15-203.us-west-2.compute.amazonaws.com
#ssh -i "key_pair.pem" ubuntu@35.164.15.203

import paramiko

class ConnectToSSH:
	def __init__(self, ip = '', key = ''):
		self.ip  = ip
		self.key = key



	def Open(self):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.client.connect(hostname='35.164.15.203',port=22,username='ubuntu',key_filename='keys/key_pair.pem')
		#comando2 = 'sudo apt-get install apache2'
		comando2 = 'sudo apt-get upgrade -b -n1'
		stdin, stdout, stder = self.client.exec_command(comando2)
		#stdin.write('Y')
		print(stdout.read())
	def Close(self):
		pass