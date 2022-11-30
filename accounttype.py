import adminpanel
import managerpanel
import clientpanel
import manager.register
import mysql.connector
import pickle

client_no = 0

def acctype():
    global client_no
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
                man_email = input('Enter email:\t')
                man_passwd = input('Enter password:\t')
                for row in results:
                    if row[5] == man_email and row[6] == man_passwd:
                        print("\nWelcome",row[1],"Manager!!")
                        managerpanel.ap()
                    else:
                        print("\nWrong password!\n")
                        break
                break

        elif a == '3':
            b = input("First time? (y/n): ")
            if b == "y":
                manager.register.ap()
            else:
                while True:
                    cred = open("cred.dat", "rb")
                    dat = pickle.load(cred)
                    cred.close()
                    Passwo = dat[0]
                    Databa = dat[1]
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password=Passwo, database=Databa)
                    cur = conn.cursor()
                    cur.execute("select * from clients")
                    results = cur.fetchall()
                    print("Please, enter your login information.")
                    cli_email = input('Email: ')
                    cli_passwd = input('Password: ')
                    for row in results:
                        if row[6] == cli_email and row[8] == cli_passwd:
                            if row[12]:
                                print("Your account is frozen!")
                            else:
                                print("\nWelcome", row[1], "!")
                                client_no = row[0]
                                clientpanel.ap()
                        else:
                            print("\nWrong email or password!")
                    break
        elif a == '0':
            print("\nShutting down the program.")
            break
        else:
            print("\nWrong input!")
