from datetime import date
import pickle
import mysql.connector

def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def ap1():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    query=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=query.cursor()
    print("-------------Add client Process-------------")

#client acc_no
    while True:
        acc_no=input("Enter accaunt_no (max 5 int): ")
        if len(acc_no) <= 5:
            try:
                acc_no=int(acc_no)
                print("Done OK")
            except ValueError:
                print("acc_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
#client account type
    while True:
        print("1.Save")
        print("2.Credit")
        a=input("Enter choice (1 or 2):")
        if a== '1':
            acc_type='S'
            break
        elif a=='2':
            acc_type='C'
            break
        else:
            print("Wrong input!!")
#client Birth date
    while True:
        while True:
            year=input("Enter birth year (4 int): ")
            if len(year) == 4:
                try:
                    year=int(year)
                    print("Done OK")
                except ValueError:
                    print("year should be an integer!!")
                else:
                    break
            else:
                print("Year consists of 4 integers!!")

        while True:
            month=input("Enter birth month (2 int) (01 to 12): ")
            if len(month) == 2:
                try:
                    month=int(month)
                    print("Done OK")
                except ValueError:
                    print("month should be an integer!!")
                else:
                    break
            else:
                print("Month consists of 2 integers!!")

        while True:
            day=input("Enter birth day (2 int) : ")
            if len(day) == 2:
                try:
                    day=int(day)
                    print("Done OK")
                except ValueError:
                    print("Date should be an integer!!")
                else:
                    break
            else:
                print("Date consists of 2 integers!!")

        try:
            birth_date=date(year,month,day)
        except ValueError:
            import traceback
            traceback.print_exc()
        else:
            if age(birth_date)>=20 and age(birth_date)<=60:
                break
            else:
                if age(birth_date)<20:
                    print("client must be atleast 20 years of age!!")
                else:
                    print("Maximum age is 60 years!!!")
                print("\nwrong input\n")
#client name          
    while True:
        first_name=input("Enter first name (max 15 char): ")
        if len(first_name)<= 15:
            break
        else:
            print("Max 15 characters")

    while True:
        last_name=input("Enter last name (max 15 char): ")
        if len(last_name)<= 15:
            break
        else:
            print("Max 15 characters")
#client Gender
    while True:
        print("1.Male")
        print("2.Female")
        a=input("Enter choice (1 or 2):")
        if a== '1':
            gender='M'
            break
        elif a=='2':
            gender='F'
            break
        else:
            print("Wrong input!!")
#client add date
    while True:
        while True:
            addyear=input("Enter add year (4 int): ")
            if len(addyear) == 4:
                try:
                    addyear=int(addyear)
                    print("Done OK")
                except ValueError:
                    print("year should be an integer!!")
                else:
                    break
            else:
                print("Year consists of 4 integers!!")

        while True:
            addmonth=input("Enter add month (2 int) (01 to 12): ")
            if len(addmonth) == 2:
                try:
                    addmonth=int(addmonth)
                    print("Done OK")
                except ValueError:
                    print("month should be an integer!!")
                else:
                    break
            else:
                print("Month consists of 2 integers!!")

        while True:
            addday=input("Enter add day (2 int) (01 to 31): ")
            if len(addday) == 2:
                try:
                    addday=int(addday)
                    print("Done OK")
                except ValueError:
                    print("Date should be an integer!!")
                else:
                    break
            else:
                print("Date consists of 2 integers!!")

        try:
            acc_creation_date=date(addyear,addmonth,addday)
        except ValueError:
            import traceback
            traceback.print_exc()
        else:
            if age(acc_creation_date)>60:
                print("client must be below 60 years of age!!")
            elif age(birth_date)-age(acc_creation_date)>=18:
                break
            else:
                print("client must atleast be 18 years of age!!")
#client phone          
    while True:
        mobile_no=input("Enter mobile (max 11 char): ")
        if len(mobile_no)<= 11:
            print("Done OK")
            break
        else:
            print("Max 11 characters")
#client email   
    while True:
        email=input("Enter email (max 25 char): ")
        if len(email)<= 25:
            print("Done OK")
            break
        else:
            print("Max 25 characters")
# client passwd
    while True:
        passwd=input("Enter manager login password(max 8 characters, min 4): ")
        lp=len(passwd)
        if lp>8:
            print("Max 8 characters only.")
        elif lp<4:
            print("Minimum 4 characters to be entered.")
        else:
            print("Done OK")
            break

    print("=========== Final Data ===========")
    print(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email,passwd)
    add_client=("INSERT INTO clients "
    "(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email,passwd) "
    "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data_client=(acc_no,acc_type,first_name,last_name,gender,birth_date,acc_creation_date,mobile_no,email,passwd)
    try:
        cur.execute(add_client, data_client)
        query.commit()
    except mysql.connector.Error as err:
        print(err.msg)
        print("-----------Value addition was unsuccessful!!!!-------------")
    # else:
    #     print("Values added successfully!!")
    #     while True:
    #         password=input("Enter manager login password(max 8 characters, min 4): ")
    #         lp=len(password)
    #         if lp>8:
    #             print("Max 8 characters only.")
    #         elif lp<4:
    #             print("Minimum 4 characters to be entered.")
    #         else:
    #             try:
    #                 cur.execute("INSERT INTO managerpass values({},LPAD({},{},'0'))".format(acc_no,password,lp))
    #                 query.commit()
    #             except mysql.connector.Error as err:
    #                 print(err.msg)
    #                 print("-----------Password addition was unsuccessful!!!!-------------")
    #             else:
    #                 print("Password added successfully!!!")
    #                 break
    cur.close()
    query.close()