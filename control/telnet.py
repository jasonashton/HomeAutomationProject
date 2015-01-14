#!/bin/python3

import socket

def sendpacket(packet):
	TCP_IP = '10.0.1.17'
	TCP_PORT = 23
	BUFFER_SIZE = 1024
	MESSAGE = packet.encode('utf-8')

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	s.close()
	return "Successful Sending"
