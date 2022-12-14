import pickle
import mysql.connector
import accounttype

acc_no = 0
credit_atm = 0

def ap():
    global credit_amt
    cred = open("cred.dat", "rb")
    dat = pickle.load(cred)
    cred.close()
    Passwo = dat[0]
    Databa = dat[1]
    query = mysql.connector.connect(
        host="localhost", user="root", password=Passwo, database=Databa)
    cur = query.cursor()

    global acc_no

    print("-------------Add client credit Process-------------")
    while True:
        acc_no = input(("Enter acc_no of the Client to edit the details: "))
        if len(acc_no) <= 5:
            try:
                acc_no = int(acc_no)
                print("Checking...")
            except ValueError:
                print("acc_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
    cur.execute("select * from clients where acc_no={}".format(acc_no))
    results = cur.fetchall()
    if results == []:
        print(results)
        print("That client number does not exist.")
    else:
        # credit type
        while True:
            print("Choose type of credit:")
            print("1.Consumer credit")
            print("2.Car credit")
            print("3.Mortgage")
            print("4.Commercial credit")
            print("5.Household credit")

            a = input("Enter choice (1 to 5):")
            if a == '1':
                credit_type = 'ConC'
                break
            elif a == '2':
                credit_type = 'CarC'
                break
            elif a == '3':
                credit_type = 'MorC'
                break
            elif a == '4':
                credit_type = 'ComC'
                break
            elif a == '5':
                credit_type = 'HousC'
                break
            else:
                print("Wrong input!!")
    # credit_amt
        while True:
            credit_amt = input("Enter credit amount: ")
            if len(credit_amt) <= 10:
                try:
                    credit_amt=int(credit_amt)
                    print("Done OK")
                except ValueError:
                    print("credit_amt should be an integer!!")
                else:
                    break
            else:
                print("credit_amt consists of 10 integers!!")
    # time_period_months
        while True:
            time_period_months = input("Enter time_period_months: ")
            if len(time_period_months) <= 10:
                try:
                    time_period_months=int(time_period_months)
                    print("Done OK")
                except ValueError:
                    print("time_period_months should be an integer!!")
                else:
                    break
            else:
                print("credit_amt consists of 10 integers!!")
    # iterest_perc_per_annum
        while True:
            iterest_perc_per_annum = input("Enter iterest_perc_per_annum: ")
            if len(iterest_perc_per_annum) <= 1:
                try:
                    iterest_perc_per_annum=int(iterest_perc_per_annum)
                    print("Done OK")
                except ValueError:
                    print("iterest_perc_per_annum should be an integer!!")
                else:
                    break
            else:
                print("credit_amt consists of 10 integers!!")
    # amt_per_month
        while True:
            amt_per_month = credit_amt/time_period_months
            break

        print("=========== Final Data ===========")
        print(credit_type, credit_amt, time_period_months,
            iterest_perc_per_annum, amt_per_month)
        add_client = ("INSERT INTO credit "
                    "(credit_type,credit_amt,time_period_months,iterest_perc_per_annum,amt_per_month) "
                    "VALUES (%s,%s,%s,%s,%s)")
        data_client = (credit_type, credit_amt, time_period_months,
                    iterest_perc_per_annum, amt_per_month)
        try:
            cur.execute(add_client, data_client)
            query.commit()
        except mysql.connector.Error as err:
            print(err.msg)
            print("-----------Value addition was unsuccessful!!!!-------------")
    cur.close()
    query.close()
    
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()
    cur.execute("select * from clients")
    results=cur.fetchall()
    print("+---------+-------------+------------------+------------------+------------+-------------+----------------+")
    print("|","%16s"%"FIRST_NAME","|","%16s"%"LAST_NAME","|","%7s"%"GENDER","|","%11s"%"BIRTH_DATE","|","%11s"%"MOBILE_NO","|","%16s"%"EMAIL","|","%7s"%"ACC_TYPE","|","%7s"%"BALANCE","|")
    for row in results:
        if accounttype.client_no == row[0]:
            try:
                money=row[11]+credit_amt
                cur.execute("update clients set money='{}' where acc_no={}".format(money,acc_no))
                conn.commit()
            except mysql.connector.Error as err:
                print(err.msg)
                print("-----------Value addition was unsuccessful!!!!-------------")
                break
            else:
                print("Updated money...")
                break
    cur.close()
    conn.close()

