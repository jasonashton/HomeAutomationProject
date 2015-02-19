'''Controls the programming of the database. Will also include the indentifying function'''
import sql

def main():
    sql.dbcheck()
    print("Do you wish to program a room or remove your database? (program/remove/mainmenu)")
    answer = input('')
    if answer == "program":
        sql.program()
    elif answer == "remove":
        sql.removedb()
    elif answer == "mainmenu":
        pass
    else:
        print("Invalid Syntax")
        main()
