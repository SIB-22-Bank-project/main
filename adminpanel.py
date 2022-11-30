import admin.addmanager
import admin.delmanager
import admin.editmanager
import admin.showmanagers
import admin.frozeclient
import manager.addclient
import manager.delclient
import manager.editclient
import manager.showclient

def ap():
    print("\nWelcome Admin!!")
    
    while True:
        print("\n---------------------Admin Panel-----------------------")
        print("\n----Managers----")
        print("1. Add a new manager")
        print("2. Delete a manager")
        print("3. Edit a manager")
        print("4. Show a manager table")
        print("----Clients----")
        print("5. Add a client")
        print("6. Del a client")
        print("7. Edit a client")
        print("8. Show a client table")
        print("9. Block a client")
        print("\nInput 0 to quit.")
        a=input("Enter choice: ")
        if a=='1':
            admin.addmanager.ap1()
        elif a=='2':
            admin.delmanager.ap2()
        elif a=='3':
            admin.editmanager.ap3()
        elif a=='4':
            admin.showmanagers.ap4()
        if a=='5':
            manager.addclient.ap()
        elif a=='6':
            manager.delclient.ap2()
        elif a=='7':
            manager.editclient.ap3()
        elif a=='8':
            manager.showclient.ap4()
        elif a=='9':
            admin.frozeclient.ap5()
        elif a=='0':
            print("Quit Admin Panel.")
            break
        else:
            print("Wrong input!(1,2,3)")