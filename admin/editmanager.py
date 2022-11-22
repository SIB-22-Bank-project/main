import mysql.connector
import pickle
from datetime import date


def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


cur = None
conn = None
manager_no = 0
add_date = None
birth_date = None


def ap3():
    global cur
    global conn
    cred = open("cred.dat", "rb")
    dat = pickle.load(cred)
    cred.close()
    Passwo = dat[0]
    Databa = dat[1]
    conn = mysql.connector.connect(
        host="localhost", user="root", password=Passwo, database=Databa)
    cur = conn.cursor()

    global manager_no
    global birth_date
    global add_date
    print("---------Edit manager process----------\n")
    while True:
        manager_no = input(("Enter manager_no to edit the details: "))
        if len(manager_no) <= 5:
            try:
                manager_no = int(manager_no)
                print("Checking...")
            except ValueError:
                print("manager_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
    cur.execute("select * from managers where manager_no={}".format(manager_no))
    results = cur.fetchall()
    if results == []:
        print(results)
        print("That manager number does not exist.")
    else:
        results1 = results[0]
        print("1.manager_no:", results1[0])
        print("2.first_name:", results1[1])
        print("3.last-name:", results1[2])
        print("4.gender:", results1[3])
        print("5.birth_date:", results1[4])
        print("6.email", results1[5])
        print("7.password:", results1[6])
        print("8.add_date:", results1[6])
        birth_date = results1[4]
        add_date = results1[6]
        f2()


def f2():
    global cur
    global conn
    global manager_no
    global birth_date
    global add_date
    print("0 to quit.")
    a = input("What would you like to change from the above:")
    if a == '2':
        while True:
            first_name = input("Enter first name (max 15 char): ")
            if len(first_name) <= 15:
                try:
                    cur.execute("update managers set first_name='{}' where manager_no={}".format(
                        first_name, manager_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated first name...")
                    break
            else:
                print("Max 15 characters")
    if a == '3':
        while True:
            last_name = input("Enter last name (max 15 char): ")
            if len(last_name) <= 15:
                try:
                    cur.execute("update managers set last_name='{}' where manager_no={}".format(
                        last_name, manager_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated last name...")
                    ap3()
            else:
                print("Max 15 characters")
    if a == '4':
        while True:
            print("1.Male")
            print("2.Female")
            a = input("Enter choice (1 or 2):")
            if a == '1':
                try:
                    cur.execute(
                        "update managers set gender='M' where manager_no={}".format(manager_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated gender...")
                    ap3()

            elif a == '2':
                gender = 'F'
                try:
                    cur.execute(
                        "update managers set gender='F' where manager_no={}".format(manager_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated gender...")
                    ap3()

            else:
                print("Wrong input!!")
    if a == '5':
        while True:
            while True:
                year = input("Enter birth year (4 int): ")
                if len(year) == 4:
                    try:
                        year = int(year)
                        print("Done OK")
                    except ValueError:
                        print("year should be an integer!!")
                    else:
                        break
                else:
                    print("Year consists of 4 integers!!")

            while True:
                month = input("Enter birth month (2 int) (01 to 12): ")
                if len(month) == 2:
                    try:
                        month = int(month)
                        print("Done OK")
                    except ValueError:
                        print("month should be an integer!!")
                    else:
                        break
                else:
                    print("Month consists of 2 integers!!")

            while True:
                day = input("Enter birth day (2 int) : ")
                if len(day) == 2:
                    try:
                        day = int(day)
                        print("Done OK")
                    except ValueError:
                        print("Date should be an integer!!")
                    else:
                        break
                else:
                    print("Date consists of 2 integers!!")

            try:
                birth_date = date(year, month, day)
            except ValueError:
                import traceback
                traceback.print_exc()
            else:
                if age(birth_date) >= 20 and age(birth_date) <= 60:
                    if age(birth_date)-age(add_date) >= 20:
                        try:
                            cur.execute("update managers set birth_date='{}' where manager_no={}".format(
                                birth_date, manager_no))
                            conn.commit()
                        except mysql.connector.Error as err:
                            print(err.msg)
                            print(
                                "-----------Value addition was unsuccessful!!!!-------------")
                            break
                        else:
                            print("Updated birth date...")
                            ap3()
                    else:
                        print("Manager must be atleast 20 years of age when hired!!")
                        print(birth_date, ": birth_date")
                else:
                    if age(birth_date) < 20:
                        print("Manager must be atleast 20 years of age!!")
                    else:
                        print("Maximum age is 60 years!!!")
                    print("\nwrong input\n")
    if a == '6':
        while True:
            email=input("Enter email (max 25 char): ")
            if len(email)<= 15:
                try:
                    cur.execute("update managers set email='{}' where manager_no={}".format(email,manager_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    break
                else:
                    print("Updated email...")
                    break
            else:
                print("Max 25 characters")
    if a == '7':
        while True:
            password = input("Enter Manager login password(max 8 characters, min 4): ")
            lp = len(password)
            if lp > 8:
                print("Max 8 characters only.")
            elif lp < 4:
                print("Minimum 4 characters to be entered.")
            else:
                try:
                    cur.execute("update managers set passwd='{}' where manager_no={}".format(
                        password, manager_no))
                    conn.commit()
                except mysql.connector.Error as err:
                    print(err.msg)
                    print("-----------Value addition was unsuccessful!!!!-------------")
                    ap3()
                else:
                    print("Password changed successfully!!!")
                    break
    cur.close()
    conn.close()
