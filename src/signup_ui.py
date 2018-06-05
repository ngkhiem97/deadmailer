from database import *

class signup_ui:

	def typing(self, string):
		return input("Enter " + string + ":")

	def run(self):
		while(True):
			username = self.typing("username")
			password = self.typing("password")
			if self.validPassword(password):
				password_again = self.typing("password again")
				if (password_again == password):
					database().updateDatabase(username, password)
					break
				else:
					print("rewite password is incorrect")
			else:
				print("password is too weak")

	def validPassword(sef, password):
		if (len(password) >= 6 and len(password) <= 60):
			return True
		else:
			return False

