import smtplib

def sendMail(useremail, password, toemail, emailsubject, emailbody):
	gmail_user = useremail  
	gmail_password = password

	sent_from = gmail_user  
	to = toemail
	subject = emailsubject
	body = emailbody

	email_text = """\r\n
	From: %s  
	To: %s  
	Subject: %s

	%s
	""" % (sent_from, to, subject, body)

	try:  
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		print('Email sent!')
	except:  
		print('Something went wrong...')