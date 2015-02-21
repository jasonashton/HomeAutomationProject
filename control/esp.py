#!/usr/bin/python3
import os
import main

def firmware():
    port = "/dev/ttyUSB0"

    print("Press enter when your esp is ready, and in firmware update mode")
    input('')

    firmwareflags = "--port " + port + " write_flash 0x000000 ../esp8266/nodemcu_latest.bin"

    os.system("../esp8266/esptool.py %s" % firmwareflags)

def luacode():
    port = "/dev/ttyUSB0"

    print("Press enter when your esp is ready")
    input('')


    luaflags = "--port " + port + " --src ../esp8266/init.lua --dest init.lua"

    os.system("../esp8266/luatool.py %s" % luaflags)
def prompt():
    print("1.firmware update\n\
2. lua upload?\n\
3. return")
    answer = input('')
    if answer == "1":
        firmware()
    elif answer == "2":
        luacode()
    elif answer == "3":
        main.start()
    else:
        print("Invalid syntax")
        prompt()
