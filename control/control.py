#!/bin/python3
import sql
import telnet

query = "WHERE "

def prompt():
    sql.dbcheck()
    print("Here is your programmed entries:")
    sql.dblist("*","")
    room()
    device()
    sql.dblist("*", query)
    print("Opening telnet...")
    ip = str(sql.dblist("IP", query))[2,-3]
    telnet.main(ip)

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
