class database:

	usernameFile = "username.db"
	passwordFile = "password.db"

	def checkUsername(self, username):
		with open(self.usernameFile) as usernameFileHandler:
			if username in usernameFileHandler.read():
				return True
			else:
				return False

	def checkPassword(self, username, password):
		with open(self.usernameFile) as usernameFileHandler:
			for num, line in enumerate(usernameFileHandler):
				if username in line:
					usernameIndex = num
		with open(self.passwordFile) as passwordFileHandler:
			for num, line in enumerate(passwordFileHandler):
				if num == usernameIndex:
					line = line.rstrip('\n')
					if line == password:
						return True
					else:
						return False

	def updateDatabase(self, username, password):
		with open(self.usernameFile, "a") as usernameFileHandler:
			usernameFileHandler.write(username + "\n")
		with open(self.passwordFile, "a") as passwordFileHandler:
			passwordFileHandler.write(password + "\n")
