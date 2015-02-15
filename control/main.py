#/bin/python3
'''
ORCA Home Automation Controller
Jason Ashton, 2015
'''
import sys
if sys.version_info < ( 3, 0):
    sys.exit('ERROR: Run with Python 3')
import program
import control
import telnet
import esp

complete = False

def mainmenu():
    print("\nWelcome to the ORCA Home Automation Controller\n\
1. Program a database\n\
2. Program an ESP\n\
3. Control a room\n\
4. Telnet directly\n\
5. Exit\n\
Enter a line number:")
    

    answer = input('').lower()

    if answer == "1":
        program.main()
    elif answer == "2":
        esp.main()
    elif answer == "3":
        control.prompt()
    elif answer == "4":
        print("IP?")
        ip = input('')
        telnet.main(ip)
    elif answer == "5" or answer == "exit":
        return "exit"
    else:
        print('Invalid Syntax')


while not complete:
    answer = mainmenu()
    if answer == "exit":
        complete = True
