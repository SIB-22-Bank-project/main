import mysql.connector
import pickle
import accounttype

def ap1():
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
    print("|","%16s"%"FIRST_NAME","|","%16s"%"LAST_NAME","|","%7s"%"GENDER","|","%11s"%"BIRTH_DATE","|","%11s"%"MOBILE_NO","|","%16s"%"EMAIL","|","%7s"%"ACC_TYPE","|")
    for row in results:
        if accounttype.client_no == row[0]:
            print("+---------+-------------+------------------+------------------+------------+-------------+----------------+")
            print("|","%16s"%row[1],"|","%16s"%row[2],"|","%7s"%row[3],"|","%11s"%row[4],"|","%11s"%row[5],"|","%16s"%row[6],"|","%7s"%row[7],"|")
    cur.close()
    conn.close()
    print("+---------+-------------+------------------+------------------+------------+-------------+----------------+")