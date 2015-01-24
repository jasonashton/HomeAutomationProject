import os

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
def main():
    print("firmware update or lua upload? (firmware/lua/mainmenu)")
    answer = input('')
    if answer == "firmware":
        firmware()
    elif answer == "lua":
        luacode()
    elif answer == "mainmenu":
        pass
    else:
        print("Invalid syntax")
        main()
