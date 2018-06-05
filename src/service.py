import threading
import time
from mailer import *

class service:

	def __init__(self):
		self.day = 0
		self.hour = 0
		self.minute = 0
		self.second = 0
		self.useremail = ""
		self.password = ""
		self.toemail = ""
		self.emailsubject = ""
		self.emailbody = ""
		self.startTime = time.clock()

	def setTime(self, day, hour, minute, second):
		self.day = day
		self.hour = hour
		self.minute = minute
		self.second = second

	def start(self):
		if (self.timeSet() and self.mailSet()):
			self.startTime = time.clock()
			self.timerThread = threading.Timer(float(self.toSec()), sendMail, [self.useremail, self.password, self.toemail, self.emailsubject, self.emailbody])
			self.timerThread.start()
			return True
		else:
			return False

	def restart(self):
		self.startTime = time.clock()
		self.timerThread.cancel()
		self.timerThread = threading.Timer(float(self.toSec()), sendMail, [self.useremail, self.password, self.toemail, self.emailsubject, self.emailbody])
		self.start()

	def setMail(self, useremail, password, toemail, emailsubject, emailbody):
		self.useremail = useremail
		self.password = password
		self.toemail = toemail
		self.emailsubject = emailsubject
		self.emailbody = emailbody

	def timeSet(self):
		if (self.day != 0 or self.hour != 0 or self.minute != 0 or self.second != 0):
			return True
		else:
			return False

	def mailSet(self):
		if (len(self.useremail) > 0 and len(self.password) > 0 or len(self.toemail) > 0 or len(self.emailsubject) > 0, len(self.emailbody) > 0):
			return True
		else:
			return False

	def toSec(self):
		return self.day*86400 + self.hour*3600 + self.minute*60 + self.second

	def getTime(self):
		return time.clock() - self.startTime
