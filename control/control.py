#!/bin/python3
import sql

query = "WHERE "

def prompt():
	sql.dbcheck()
	print("Press enter if you know the room, or 'list' to list the rooms you have programmed (enter/list/mainmenu)")
	answer = input('')
	if answer == "list":
		sql.list("")
		prompt()
	elif answer == "mainmenu":
        	pass
	else:
		room()
		device()
		sql.list(query)

def room():
	global query
	print("Please enter the room you'd like")
	room = input('')
	query = query +("room = '%s' and " % room)

def device():
	global query
	print("Please type the device")
	device = input('')
	query = query + ("device = '%s'" % device)
