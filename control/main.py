#/bin/python3
'''
ESP Home Automation Controller
Jason Ashton, 2015
'''
import program
import control

def mainmenu():
	print("Welcome to the ESP Home Automation Controller. Do you wish to:\
	program a room or control one? (program/control)")
	
	answer = input('').lower()
	
	if answer == "program":
		return "program"
	elif answer == "control":
		return "control"
	else:
		print('Invalid Syntax')
		mainmenu()

	

answer = mainmenu()
if answer == "program":
	program.prompt()
elif answer == "control":
	control.prompt()

