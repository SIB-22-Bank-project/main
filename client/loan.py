import mysql.connector
import pickle
def ap3():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()
    cur.execute("select * from loan")
    results=cur.fetchall()
    print("+---------+-------------+------------------+------------------+---------+------------------+------------------+")
    print("|","%7s"%"ACC_NO","|","%11s"%"LOAN_TYPE","|","%11s"%"lOAN_AMT","|","%20s"%"TIME_PERIOD_MONTHS","|","%11s"%"IT_P_P_A","|","%11s"%"AMT_P_M","|","%17s"%"REMAINING_AMT","|")
    for row in results:
        print("+---------+-------------+------------------+------------------+---------+------------------+------------------+")
        print("|","%7s"%row[0],"|","%11s"%row[1],"|","%11s"%row[2],"|","%20s"%row[3],"|","%11s"%row[4],"|","%11s"%row[5],"|","%17s"%row[6],"|")
    cur.close()
    conn.close()
    print("+---------+-------------+------------------+------------------+---------+------------------+------------------+")