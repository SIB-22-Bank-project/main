import pickle
import mysql.connector

acc_no = 0


def ap():
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
            if len(credit_amt) <= 11:
                try:
                    credit_amt = int(credit_amt)
                    print("Checking...")
                except ValueError:
                    print("credit_amt should be an integer!!")
                else:
                    break
    # time_period_months
        while True:
            time_period_months = input("Enter credit amount: ")
            if len(time_period_months) <= 11:
                try:
                    time_period_months = int(time_period_months)
                    print("Checking...")
                except ValueError:
                    print("time_period_months should be an integer!!")
                else:
                    break
    # iterest_perc_per_annum
        while True:
            iterest_perc_per_annum = input("Enter credit amount: ")
            if len(iterest_perc_per_annum) <= 1:
                try:
                    iterest_perc_per_annum = int(iterest_perc_per_annum)
                    print("Checking...")
                except ValueError:
                    print("iterest_perc_per_annum should be an integer!!")
                else:
                    break
    # amt_per_month
        while True:
            amt_per_month = credit_amt/time_period_months
            break

        print("=========== Final Data ===========")
        print(credit_type, credit_amt, time_period_months,
            iterest_perc_per_annum, amt_per_month)
        add_client = ("INSERT INTO clients "
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
