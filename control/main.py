#/bin/python3
'''
ORCA Home Automation Controller
Jason Ashton, 2015
'''
import sys
if sys.version_info < ( 3, 0):
	sys.exit('ERROR: Run with Python 3')
import program
import control

quit = False

def mainmenu():
	print("Welcome to the ORCA Home Automation Controller. Do you wish to:\
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
	    program.main()
    elif answer == "control":
        control.prompt()
    elif answer == "exit":
        quit = True
