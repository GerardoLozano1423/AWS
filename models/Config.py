from models.InstallServe import InstallServe
from models.ConnectToSSH import ConnectToSSH


class Config(ConnectToSSH, InstallServe):
	def Install(self):
		pass