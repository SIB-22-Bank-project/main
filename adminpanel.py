import admin.addmanager
import admin.delmanager
import admin.editmanager
import admin.showmanagers

def ap():
    print("\nWelcome Admin!!")
    
    while True:
        print("\n---------------------Admin Panel-----------------------")
        print("\n1.Add manager")
        print("2.Del manager")
        print("3.Edit manager")
        print("4.Show manager table")
        print("\nInput 0 to quit.")
        a=input("Enter choice:")
        if a=='1':
            admin.addmanager.ap1()
        elif a=='2':
            admin.delmanager.ap2()
        elif a=='3':
            admin.editmanager.ap3()
        elif a=='4':
            admin.showmanagers.ap4()
        elif a=='0':
            print("Quit Admin Panel.")
            break
        else:
            print("Wrong input!(1,2,3)")