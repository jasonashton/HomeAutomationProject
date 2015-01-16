'''Controls the programming of the database. Will also include the indentifying function'''
import sql
import os

def update():
	print("Please verify the room you're looking for isn't on this list")
	sql.list("")
	print("Continue? (y/n)")
	answer = input("")
	if answer == "y":
		sql.program()

def removedb():
	sql.removedb()

def main():
	sql.dbcheck()
	print("Do you wish to update or remove your database? (update/remove/mainmenu)")
	answer = input('')
	if answer == "update":
		update()
	elif answer == "remove":
		removedb()
	elif answer == "mainmenu":
		return "hello"
	else:
		print("Invalid Syntax")
		main()
