import sys
class customer:
    bankname='anandbank'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposite(self,amt):
        self.balance=self.balance+amt
        print('balance after deposite',self.balance)
    def widraw(self,amt):
        if amt>self.balance:
            print('infuicent balance found...annot perform this operation')
            sys.exit()
            self.balance=self.balance-amt
            print('balance after widraw',self.balanc)
            print('welcome to',customer.bankname)
            name=input('enter your name; ')
        while True:
            print('d-Deposit \nw-witdraw\ne-exist')
            option=input('choose option')
            if option=='d' or option=='D':
                amt=float(input('enter amont'))
                c.deposit(amt)
            elif option=='w' or option=='W':
                amt=float(input('enter amont'))
                c.widraw(amt)
            elif option=='e' or option=='E':
                print('thank for banking')
                sys.exit()

            else:
                print('INVALID  OPTION .. PLZ CHOOSE VALID OPTION')
a1=customer()
print(a1)
