from service import *

class main_ui():

	TIME_CONST = 10000
	deadMail = service()

	def typing(self, string):
		return input("Enter " + string + ":")

	def displayOptions(self, options):
		print("Choose these following options")
		for option in options:
			print(option)
		print("Time passed: " + str(self.deadMail.getTime()*self.TIME_CONST) + " sec")

	def run(self):
		while True :
			options = ["1.set time", "2.set email", "3.start", "4.restart", "5.display time"]
			self.displayOptions(options)
			userOptions = int(self.typing("option"))
			if userOptions == 1:
				day = self.typing("day")
				hour = self.typing("hour")
				minute = self.typing("minute")
				second = self.typing("second")
				self.deadMail.setTime(int(day), int(hour), int(minute), int(second))
			elif userOptions == 2:
				useremail = self.typing("useremail")
				password = self.typing("password")
				toemail = self.typing("toemail")
				emailsubject = self.typing("email subject")
				emailbody = self.typing("email body")
				self.deadMail.setMail(useremail, password, toemail, emailsubject, emailbody)
			elif userOptions == 3:
				self.deadMail.start()
			elif userOptions == 4:
				self.deadMail.restart()
			elif userOptions == 5:
				print("Time passed: " + str(self.deadMail.getTime()*self.TIME_CONST) + " sec")
			else:
				print("unavailable option please choose again")