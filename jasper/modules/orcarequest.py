import re
import os

WORDS = ["TURN", "ON", "OFF"]

global room = " "
global device = " "
global status = " "
global speak = " "

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bturn\b', text, re.IGNORECASE))
	

'''def getrequest():
    text = raw_input("What do you need?")
    createarray(text)

def checkarray(text):
    if len(request) == 4:

eventaully use this to create multiple accepted requests that all mean the same thing but said differently
'''

def getrequest():
    global speak
    speak.say("What do you want to do?")
    text = speak.activeListen()
    createarray(text3)

def createarray(text):
    request = text.split()
    getroom(request)

def getroom(request):
    global room
    room = request[2]
    getdevice(request)

def getdevice(request):
    global device
    postion = request[3]
    appliance = request[4]
    device = "%s_%s" %(postion, applaence)
    getstatus(request)

def getstatus(request):
    global status
    status = request[1]
    checkstatus()

def checkstatus():
    global status 
    global speak
    if status == "on":
        sendrequest()
    if status == "off":
        sendrequest()
    else:
        speak.say ("error, please specify status")
        getrequest()

def sendrequest():
    global status
    global device
    global room
    global speak

    speak.say("turning %s %s %s" %(status, room, device))

    #print status
    #print device
    #print room
    #os.chdir(r'/home/pi/orca')
    
    os.startfile('~/ORCA-Home-Automation/control/main.py -r %s -d %s -s %s > test.txt" %(room, device, status)')
    speak.say("%s %s turned %s bitch" %(room, device, status))
    
    #print "main.py -r %s -d %s -s %s" %(room, device, status)

def handle(text, mic, profile):
    global speak
    speak = mic 
    createarray(text)



#Room, device, intended status   turn on bedroom desk lamp 


