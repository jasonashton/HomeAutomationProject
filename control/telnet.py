#/!usr/bin/python3

import main
import socket

def sendpacket(ip, packet):
    TCP_IP = ip
    TCP_PORT = 23
    MESSAGE = packet.encode('utf-8')
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        s.close()
        return "Successful Sending"
    
    except OSError:
        print("Error sending. Check your parameters and the device itself.")
        main.start()


def prompt(ip):
    print("What is the message?")
    message = input('')
    sendpacket(str(ip), message)
