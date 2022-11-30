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
    cur.execute("select * from clients")
    results=cur.fetchall()
    print("+---------+-------------+------------------+------------------+---------+-------------+-------------+-------------+-------------+-------------+")
    print("|", "%7s" % "ACC_NO", "|", "%16s" % "FIRST_NAME", "|", "%16s" % "LAST_NAME", "|", "%7s" % "GENDER", "|", "%11s" % "BIRTH_DATE",
          "|", "%11s" % "MOBILE_NO", "|", "%11s" % "EMAIL", "|", "%7s" % "ACC_TYPE", "|", "%11s" % "PASSWD", "|", "|", "%7s" % "IS_FROZEN", "|")
    for row in results:
        print("+---------+-------------+------------------+------------------+---------+-------------+-------------+-------------+-------------+-------------+")
        print("|", "%7s" % row[0], "|", "%16s" % row[1], "|", "%16s" % row[2], "|", "%7s" % row[3], "|", "%11s" % row[4],
              "|", "%11s" % row[5], "|", "%11s" % row[6], "|", "%7s" % row[7], "|", "%11s" % row[8], "|", "|", "%7s" % row[12], "|")
    cur.close()
    conn.close()
    print("+---------+-------------+------------------+------------------+---------+-------------+-------------+-------------+-------------+-------------+")