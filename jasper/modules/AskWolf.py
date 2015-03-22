import re
import urllib2
appid = "L9U9Y6-4HQLKXX8JR"

WORDS = ["I", "HAVE", "A" "QUESTION"]

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bi have a question\b', text, re.IGNORECASE))

def getresponse(question, mic): #this sends the question to the server and retrieves a response

    #mic.say("requesting an answer.")
    Input = question.replace(" ", "%20") # urlencoding works better
    url = ("http://api.wolframalpha.com/v2/query?appid=%s&input=%s&format=plaintext&podindex=2" %(appid, Input))
    response = urllib2.urlopen(url)
    #mic.say("recieved an answer")
    getanswer(response, mic)

def getanswer(response, mic): #this constructs the answer by finding the answer among the response the server sends back

    reply = response.read()
    count = reply.find("plaintext") + 10
    twocount = reply.rfind("plaintext") - 2
    answer = reply[count:twocount]
    mic.say("let me check.")
    checkanswer(answer, mic)

def checkanswer(answer, mic): #this checks the answer to insure it did not recieve the wrong info

    length = len(answer)
    if length < 300:
        mic.say(answer)
    else:
        mic.say("I'm sorry, I don't know.")


def handle(text, mic, profile):

    mic.say("How Can I help you?")
    question = mic.activeListen()
    #mic.say(question)
    getresponse(question, mic)
