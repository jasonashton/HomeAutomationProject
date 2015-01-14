import sqlite3
import os
import sys

database = "rooms.sqlite"
dbloc = ',.' + database
table = "rooms"

def entry(number, name):
    conn = sqlite3.connect(dbloc)
    c = conn.cursor()
    
    c.execute("INSERT INTO rooms VALUES (%d,'%s')" % (number, name))
    
    conn.commit()
    conn.close

def createdb():
	file = open(database, 'w')
	file.close()

	conn = sqlite3.connect(dbloc)
	c = conn.cursor()
	
	c.execute("CREATE TABLE rooms (number integer, name test)")
	entry(1, "jason_bedroom")
	entry(2, "living_room")
	print("Created Database with Default Values")
	
	for row in c.execute('SELECT * FROM rooms'):
		print(row)
	
	conn.commit()
	conn.close()
	
def program():
    print("What is the name of the room you wish to add?")
    room = input('')
    print("What is the number you'd like to assign?")
    number = input('')
    entry(int(number), room)
    print("Entry successful")
    
	

def list(col):
	conn = sqlite3.connect(dbloc)
	c = conn.cursor()
	
	for row in c.execute('SELECT * FROM rooms'):
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
