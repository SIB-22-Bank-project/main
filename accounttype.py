import adminpanel
import managerpanel
import clientpanel
import manager.register
def acctype():
    while True:
        print("--------------Account Selector Menu--------------")
        print("1.Admin.")
        print("2.Manager.")
        print("3.Client.")
        print("4.Crate account.")
        print("Enter 0 to end process.")
        a = input("\nEnter your account type: ")

        if a == '1':
            b = input("\nEnter admin password: ")
            if b == "admin123":
                adminpanel.ap()
            else:
                print("\nWrong password!\n")

        elif a == '2':
            b = input("\nEnter manager password: ")
            if b == 'man123':
                managerpanel.ap()
            else:
                print("\nWrong password!\n")

        elif a == '3':
            b = input("\nDo you have an existing account? (y/n): ")
            if b == "y":
                b = input("\nPlease, enter your phone number: ")
                p = input("\nEnter your password: ")
                # тута запрос в базу
            else:
                b = input("\nDo you want to create a new account? (y/n): ")
                if b == "y":
                    manager.addclient.ap1()
            # if b == 'client123':
            #    clientpanel.ap()
            # else:
            #   print("\nWrong password!\n")b = input("\nEnter client password:")
        elif a == '4':
            manager.register.ap()
        elif a == '0':
            print("\nShutting down the program.")
            break
        else:
            print("\nWrong input!")
