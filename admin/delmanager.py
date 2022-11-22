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
    print("---------Del managers process----------\n")
    while True:
        manager_no=input(("Enter manager_no of the manager to fire them: "))
        if len(manager_no) <= 5:
            try:
                manager_no=int(manager_no)
                print("Checking...")
            except ValueError:
                print("manager_no should be an integer!!")
            else:
                break
        else:
            print("Maximum length is 5!")
    
    query="delete from managers where manager_no = {}".format(manager_no)
    cur.execute("select manager_no from managers")
    record=cur.fetchall()
    changed=False
    for r in record:
        if r[0]==manager_no:
            try:
                cur.execute(query)
                conn.commit()
                changed=True
            except mysql.connector.Error as err:
                print(err.msg)
                print("-----------Value deletion was unsuccessful!!!!-------------\n")
            else:
                print("Manager del successfully...\n")
    if not changed:
        print("The manager number does not exist.")
        print("------------Could not del manager-----------\n")
    cur.close()
    conn.close()