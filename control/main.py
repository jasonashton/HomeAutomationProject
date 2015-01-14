#/bin/python3
'''
ESP Home Automation Controller
Jason Ashton, 2015
'''
import program
import control
import sys

quit = False

def mainmenu():
	print("Welcome to the ESP Home Automation Controller. Do you wish to:\
	program a room or control one? (program/control/exit)")
	
	answer = input('').lower()
	
	if answer == "program":
		return "program"
	elif answer == "control":
		return "control"
	elif answer == "exit":
	    return "exit"
	else:
		print('Invalid Syntax')

	
while not quit:
    answer = mainmenu()
    if answer == "program":
	    program.prompt()
    elif answer == "control":
        control.prompt()
    elif answer == "exit":
        quit = True
