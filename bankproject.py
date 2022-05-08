
import sys
class customer:
    bankname="minibank"
    def _init_(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after deposit: ",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Isufficient Funds.. Cannot perform this operation")
            sys.exit()
            self.balance=self.balance-amt
            print("Balance after withdraw:",self.balance)
        print("Welcome to",customer.bankname)
        name=input("Enter Your Name:")
        c=customer(name)
        while True:
            print("d-Deposit \nw-Withdraw \ne-exit")
            option=input("Choose Your Option")
            if option=='d' or option=='D':
                amt=float(input("Enter your amount:"))
                c.deposit(amt)
            elif option=='w' or option=='W':
                amt=float(input("Enter amount:"))
                c.withdraw(amt)
            elif option=='e' or option=='E':
                print("thanks For Banking")
                sys.exit()
            else:
                print("Invalid Option.. Plz valid option")
a=customer('anand')
a.deposit(4000)
a.withdraw(555)