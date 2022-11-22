import adminpanel
import managerpanel
import clientpanel
import manager.register
import mysql.connector
import pickle


def acctype():
    while True:
        print("--------------Account Selector Menu--------------")
        print("1. Admin.")
        print("2. Manager.")
        print("3. Client.")
        print("Enter 0 to end process.")
        a = input("\nEnter your account type: ")

        if a == '1':
            b = input("\nEnter admin password: ")
            if b == "admin123":
                adminpanel.ap()
            else:
                print("\nWrong password!\n")

        elif a == '2':
            while True:
                cred = open("cred.dat", "rb")
                dat = pickle.load(cred)
                cred.close()
                Passwo = dat[0]
                Databa = dat[1]
                conn = mysql.connector.connect(
                    host="localhost", user="root", password=Passwo, database=Databa)
                cur = conn.cursor()
                cur.execute("select * from managers")
                results = cur.fetchall()
                email = input('Enter email:\t')
                passwd = input('Enter password:\t')
                for row in results:
                    if row[5] == email and row[6] == passwd:
                        print("\nWelcome ", row[1], "  Manager!!")
                        managerpanel.ap()
                    else:
                        print("\nWrong password!\n")

        elif a == '3':
            while True:
                cred = open("cred.dat", "rb")
                dat = pickle.load(cred)
                cred.close()
                Passwo = dat[0]
                Databa = dat[1]
                conn = mysql.connector.connect(
                    host="localhost", user="root", password=Passwo, database=Databa)
                cur = conn.cursor()
                cur.execute("select * from managers")
                results = cur.fetchall()
                email = input('Enter email:\t')
                passwd = input('Enter password:\t')
                for row in results:
                    if row[5] == email and row[6] == passwd:
                        print("\nWelcome ", row[1], "!!")
                        clientpanel.ap()
                    else:
                        print("\nWrong email or password!")
                        b = input("\nDo you want to create a new account? (y/n): ")
                        if b == "y":
                            manager.register.ap()
                        elif b == "n":
                            break
        elif a == '0':
            print("\nShutting down the program.")
            break
        else:
            print("\nWrong input!")
