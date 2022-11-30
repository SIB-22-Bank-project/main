import mysql.connector
import pickle
from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

cur=None
conn=None
acc_no=0
add_date=None
birth_date=None
def ap5():
    global cur
    global conn
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()

    global acc_no
    global birth_date
    global add_date
    print("---------Block client process----------\n")
    while True:
        acc_no=input(("Enter acc_no of the Client to edit the details: "))
        if len(acc_no) <= 5:
            try:
                acc_no=int(acc_no)
                print("Checking...")
            except ValueError:
                print("acc_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
    cur.execute("select * from clients where acc_no={}".format(acc_no))
    results=cur.fetchall()
    if results == []:
        print(results)
        print("That client number does not exist.")
    else:
        results1=results[0]
        print("1.is_frozen:",results1[12])
        birth_date=results1[1]
        add_date=results1[5]
        f2()

def f2():
    global cur
    global conn
    global acc_no
    global birth_date
    global add_date
    print("0 to quit.")
    a=input("What would you like to change from the above:")
    if a == '5':
        while True:
            print("1. Block client")
            print("2. Unblock client")
            a=input("Enter choice (1 or 2):")
            if a== '1':
                try:
                    cur.execute("update Clients set is_frozen=true where acc_no={}".format(acc_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
            elif a=='2':
                try:
                    cur.execute("update Clients set is_frozen=false where acc_no={}".format(acc_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break

            else:
                print("Wrong input!!")
    cur.close()
    conn.close()