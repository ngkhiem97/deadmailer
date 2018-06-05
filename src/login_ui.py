from database import *

class login_ui:

	def typing(self, string):
		return input("Enter " + string + ":")

	def run(self):
		while True:
			username = self.typing("username")
			if database().checkUsername(username):
				password = self.typing("password")
				if database().checkPassword(username, password):
					break
				else:
					print("incorrect password")
			else:
				print("incorrect username")