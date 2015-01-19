'''Controls the SQLite interfaces'''

import sqlite3
import os
import sys

database = "rooms.sqlite"
dbloc = ',.' + database
table = "rooms"

def entry(room, device, ip, status):
    conn = sqlite3.connect(dbloc)
    c = conn.cursor()
    
    c.execute("INSERT INTO rooms VALUES ('%s', '%s', '%s', '%s')" % (room, device, ip, status))
    
    conn.commit()
    conn.close

def createdb():
	file = open(database, 'w')
	file.close()

	conn = sqlite3.connect(dbloc)
	c = conn.cursor()
	
	c.execute("CREATE TABLE rooms (room text, device text, IP text, status text)")
	entry("your_bedroom", "lamp", "10.0.1.17", "OFF")
	entry("living_room", "lamp", "10.0.1.18", "ON")
	print("Created Database with Sample Values")
	
	for row in c.execute('SELECT * FROM rooms'):
		print(row)
	
	conn.commit()
	conn.close()
	
def removedb():
	print("You are about to remove your database.\
	\nThere is no turning back. Are you sure? (y/n)")
	answer = input('')
	if answer == "y":
		os.remove("./%s" % dbloc)
		os.remove("./%s" % database)
def program():
    print("What is the name of the room you wish to add?")
    room = input('')
    print("What is the number you'd like to assign?")
    number = input('')
    entry(int(number), room)
    print("Entry successful")
    
	

def list(opt):
	conn = sqlite3.connect(dbloc)
	c = conn.cursor()
	
	for row in c.execute("SELECT * FROM rooms %s" % opt):
	#	print(str(row)[2:-3])
		print(row)

	conn.commit()
	conn.close()

def dbcheck():
    if os.access(database, os.R_OK):
	    return "Success"
    else:
        print("No Database found. Do you wish to create one? (y/n)")
        answer = input('')
        if answer == "y":
	        createdb()
        elif answer == "n":
            sys.exit('Declined to create DB')
        else:
            dbcheck()
