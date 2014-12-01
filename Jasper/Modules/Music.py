import os
import re

WORDS = ["MUSIC"]

def handle(text)
	
	os.system("oxmplayer -o local /Home/pi/HomeAutomationProject/Jasper/Warpigs.mp3")



def isValid(text):
    """
        Returns True if input is related to the music.
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bmusic\b', text, re.IGNORECASE))