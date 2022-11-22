import manager.addclient
import manager.delclient
import manager.editclient
import manager.showclient
import mysql.connector
import pickle


def ap():
    while True:
        print("\n---------------------Manager  Panel-----------------------")
        print("\n1. Add a client")
        print("2. Del a client")
        print("3. Edit a client")
        print("4. Show a client table")
        print("\nInput 0 to quit.")
        a = input("Enter choice: ")
        if a == '1':
            manager.addclient.ap1()
        elif a == '2':
            manager.delclient.ap2()
        elif a == '3':
            manager.editclient.ap3()
        elif a == '4':
            manager.showclient.ap4()
        elif a == '0':
            print("Quit Manager Panel.")
            break
        else:
            print("Wrong input!(1,2,3)")
