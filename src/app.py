from login_ui import*
from signup_ui import *
from main_ui import *

print("      &&&&      ")
print("      &&&&      ")
print("      &&&&      ")
print("&&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&")
print("      &&&&      ")
print("      &&&&     Welcome to the deathnotes!!! ")
print("      &&&&      ")
print("      &&&&     This program will send your  ")
print("      &&&&     death testament to your love ")
print("      &&&&     ones. ")
print("      &&&&      ")
print("      &&&&      ")


while True:	
	print("Press 1 to login, press 2 to signup")
	user = input("Enter: ")
	if int(user) == 1:
		login_ui().run() 
		main_ui().run()
	elif int(user) == 2:
		signup_ui().run()