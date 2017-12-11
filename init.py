import sys
from models.Config import Config


from models.ValidateValues import ValidateValues
from models.ConnectToSSH import ConnectToSSH

Validate = ValidateValues(sys.argv)

if Validate.errorMessage != '':
	print(Validate.errorMessage)
else:
	Connect = ConnectToSSH(Validate.ip,Validate.key)
	Connect.Open()

