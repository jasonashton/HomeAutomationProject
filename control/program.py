'''Controls the programming of the database. Will also include the indentifying function'''
import sql
import os
import esp

def program():
	'''
	print("Will the device reside in one of these already-programmed rooms?")
	sql.list("")
	print("(y/n)")
	answer = input('')
	if answer == "n":
		print("What is the name of the room this device will be in?")
		room = input('')
		print("You said: " + room)'''
	esp.main()
def removedb():
	sql.removedb()

def main():
	sql.dbcheck()
	print("Do you wish to program a device or remove your database? (program/remove/mainmenu)")
	answer = input('')
	if answer == "program":
		program()
	elif answer == "remove":
		removedb()
	elif answer == "mainmenu":
		return "hello"
	else:
		print("Invalid Syntax")
		main()
