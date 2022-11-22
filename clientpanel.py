import client.account
import client.deposit
import client.credit


def ap():
    
    while True:
        print("\n---------------------Client Panel-----------------------")
        print("\n1. Account info")
        print("2. Deposit")
        print("3. Loan")
        print("\nInput 0 to quit.")
        a=input("Enter choice: ")
        if a=='1':
            client.account.ap1()
        elif a=='2':
            client.deposit.ap2()
        elif a=='3':
            client.credit.ap3()
        elif a=='0':
            print("Quit Manager Panel.")
            break
        else:
            print("Wrong input!(1,2,3)")