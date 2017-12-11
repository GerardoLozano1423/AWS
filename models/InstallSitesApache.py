class InstallSitesApache:
	def InstallSites(self):
		comando2 = 'sudo apt-get install apache2'
		stdin, stdout, stder = self.client.exec_command(comando2)
		stdin.write('Y')
		print(stdout.readlines())
		
	def ActiveSites(self):
		pass