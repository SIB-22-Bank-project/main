import mysql.connector
import pickle
def ap2():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()
    cur.execute("select * from deposit")
    results=cur.fetchall()
    print("+---------+-------------+------------------+")
    print("|","%7s"%"ACC_NO","|","%11s"%"BALANCE","|","%11s"%"PERCENT","|")
    for row in results:
        print("+---------+-------------+------------------+")
        print("|","%7s"%row[0],"|","%11s"%row[1],"|","%11s"%row[2],"|")
    cur.close()
    conn.close()
    print("+---------+-------------+------------------+")