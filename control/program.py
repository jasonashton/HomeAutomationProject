#!/bin/python3
import sql

def prompt():
    sql.dbcheck()
    print("Please verify the room you're looking for isn't on this list")
    sql.list("")
    print("Continue? (y/n)")
    answer = input("")
    if answer == "y":
        sql.program()
