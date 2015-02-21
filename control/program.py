#!/usr/bin/python3
'''Controls the programming of the database. Will also include the indentifying function'''
import sql
import main

def prompt():
    sql.dbcheck()
    print("Do you wish to:\n\
    1. add a room\n\
    2. remove a room\n\
    3. update a room\n\
    4. remove your database?\n\
    5. return")
    answer = input('')
    if answer == "1":
        sql.program()
    elif answer == "2":
        print("Not yet supported.")
    elif answer == "3":
        print("Not yet supported.")
    elif answer == "4":
        sql.removedb()
    elif answer == "5":
        main.start()
    else:
        print("Invalid Syntax")
        prompt()
