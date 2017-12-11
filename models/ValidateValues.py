import socket
import os.path as path


class ValidateValues:
	def __init__(self, argv):
		self.continueProcess = True
		self.errorMessage = ""


		#Validate IP
		if argv[1][0:4] == '-ip:':
			self.ip = argv[1][4:len(argv[1])]

			#Guardar Log
		elif argv[1][0:3] == 'ip:':
			self.ip = argv[1][3:len(argv[1])]

			#Guardar Log
		else:
			self.errorMessage = "Atributo IP Incorrecto (-ip: o ip:) \n"
			self.continueProcess = False
			#Guardar Log




		#Validate Key
		if argv[2][0:5] == '-key:':
			self.key = argv[2][5:len(argv[2])]

			#Guardar Log
		elif argv[2][0:4] == 'key:':
			self.key = argv[2][4:len(argv[2])]

			#Guardar Log
		else:
			self.errorMessage += "Atributo KEY Incorrecto (-key: o key:) \n"
			self.continueProcess = False

			#Guardar Log

		if (self.continueProcess == True):
			self.ValidateIp()
			self.ValidateKey()

			

	def ValidateIp(self):
		try:
			socket.inet_aton(self.ip)
		except socket.error:
			self.errorMessage += "IP Incorrecto ("+self.ip+") \n"


			#Guardar Log

	def ValidateKey(self):
		if self.key[0:1] == "/":
			if (path.exists(self.key)):
				pass
			else:
				self.errorMessage += "Key no encontrada"


				#Guardar Log
		else:
			if (path.exists("keys/"+self.key)):
				self.key = "keys/"+self.key
			else:
				self.errorMessage += "Key no encontrada"


				#Guardar Log