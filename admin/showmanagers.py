import mysql.connector
import pickle
def ap4():
    cred = open("cred.dat","rb")
    dat=pickle.load(cred)
    cred.close()
    Passwo=dat[0]
    Databa=dat[1]
    conn=mysql.connector.connect(host="localhost",user="root",password=Passwo,database=Databa)
    cur=conn.cursor()
    cur.execute("select * from managers")
    results=cur.fetchall()
    print("+---------+-------------+------------------+------------------+---------+-------------+----------+-------+")
    print("|","%11s"%"MANAGER_NO","|","%16s"%"FIRST_NAME","|","%16s"%"LAST_NAME","|","%7s"%"GENDER","|","%11s"%"BIRTH_DATE","|","%11s"%"PASSWD","|","%11s"%"ADD_DATE","|")
    for row in results:
        print("+---------+-------------+------------------+------------------+---------+-------------+----------+-------+")
        print("|","%11s"%row[0],"|","%16s"%row[1],"|","%16s"%row[2],"|","%7s"%row[3],"|","%11s"%row[4],"|","%11s"%row[5],"|","%11s"%row[6],"|")
    cur.close()
    conn.close()
    print("+---------+-------------+------------------+------------------+---------+-------------+----------+-------+")