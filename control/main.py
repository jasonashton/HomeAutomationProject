#!/usr/bin/python3
'''
ORCA Home Automation Controller
Jason Ashton, 2015
'''
import sys
if sys.version_info < ( 3, 0):
    sys.exit('ERROR: Run with Python 3')
import argparse
import program
import control
import telnet
import esp

complete = False
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--room", help="specify room", default="nul")
parser.add_argument("-d", "--dev", help="specify device")
parser.add_argument("-s", "--status", help="specify desired status")
args = parser.parse_args()

def start():
    print("\nWelcome to the ORCA Home Automation Controller\n\
1. Program a database\n\
2. Program an ESP\n\
3. Control a room\n\
4. Telnet directly\n\
5. Exit\n\
Enter a line number:")
    

    answer = input('').lower()
    selection(answer)

def selection(answer):
    if answer == "1":
        program.prompt()
    elif answer == "2":
        esp.prompt()
    elif answer == "3":
        control.prompt()
    elif answer == "4":
        print("IP?")
        ip = input('')
        telnet.prompt(ip)
    elif answer == "5" or answer == "exit":
        sys.exit(0)
    else:
        print('Invalid Syntax')

if __name__ == "__main__":
    if args.room != "nul":
        print("You want to turn {:s} the {:s} in the {:s}".format(args.status, args.dev, args.room))
    start()
