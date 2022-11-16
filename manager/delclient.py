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
    print("---------Del clients process----------\n")
    while True:
        acc_no=input(("Enter acc_no of the manager to fire them: "))
        if len(acc_no) <= 5:
            try:
                acc_no=int(acc_no)
                print("Checking...")
            except ValueError:
                print("acc_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
    
    query="delete from clients where acc_no = {}".format(acc_no)
    cur.execute("select acc_no from clients")
    record=cur.fetchall()
    changed=False
    for r in record:
        if r[0]==acc_no:
            try:
                cur.execute(query)
                conn.commit()
                changed=True
            except mysql.connector.Error as err:
                print(err.msg)
                print("-----------Value deletion was unsuccessful!!!!-------------\n")
            else:
                print("Client del successfully...\n")
    if not changed:
        print("The client number does not exist.")
        print("------------Could not del client-----------\n")
    cur.close()
    conn.close()