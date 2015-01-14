#!/bin/python3
import sql

def prompt():
    sql.dbcheck()
    print("Please enter the room, or 'list' to list the rooms you have programmed (room/list/mainmenu)")
    answer = input('')
    print("You entered: %s" % answer)
    if answer == "list":
        sql.list("room")
        prompt()
    elif answer == "mainmenu":
        return ""
    else:
        print("Answer not recognized")
        prompt() 
