import mysql.connector
import pickle
import accounttype

acc_no=0

def ap1():
    global acc_no
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
            print("+---------+-------------+------------------+------------------+------------+-------------+----------------+")
            print("|","%16s"%row[1],"|","%16s"%row[2],"|","%7s"%row[3],"|","%11s"%row[4],"|","%11s"%row[5],"|","%16s"%row[6],"|","%7s"%row[7],"|","%7s"%row[11],"|")
            print("+---------+-------------+------------------+------------------+------------+-------------+----------------+")
            money_func = input('Do you want to work with money?(y/n):\t')
            if money_func == 'y':
                do = input("Deposit or Withdraw(d/w):\t")
                while True:
                    acc_no = row[0]
                    new_m=input("Enter money (max 10 char): ")
                    if len(new_m)<= 10:
                        try:
                            new_m=int(new_m)
                            if do == 'd': 
                                money=row[11]+new_m
                            elif do == 'w':
                                money=row[11]-new_m

                            cur.execute("update clients set money='{}' where acc_no={}".format(money,acc_no))
                            conn.commit()
                        except mysql.connector.Error as err:
                            print(err.msg)
                            print("-----------Value addition was unsuccessful!!!!-------------")
                            break
                        else:
                            print("Updated money...")
                            break
                    else:
                        print("Max 11 characters")
    cur.close()
    conn.close()
