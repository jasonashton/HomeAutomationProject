import os
import re

WORDS = ["STOP", "WAR", "PIGS"]

def handle(text)
	
	os.system ("ps -A | grep oxmplayer") 
	os.system ("kill -9 PID") 



def isValid(text):
    """
        Returns True if input is related to the music.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bstop war pigs\b', text, re.IGNORECASE))