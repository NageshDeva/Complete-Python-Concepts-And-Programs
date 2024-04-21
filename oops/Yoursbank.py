import sys
class customer:
    bankname = 'YOURSBANK'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance+amt
        print('Balance after deposit:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('insufficient Balance..')
            sys.exit()
        self.balance = self.balance-amt
        print('Balance after withdraw:',self.balance)

print('welcome to',customer.bankname)
name = input('Enter your Name:')
c = customer(name)
while True:
    print('d-Deposit \n w-withdraw \n e-Exit')
    option = input('Choose Your Option:')
    if option =='d' or option == 'D':
        amt = float(input('Enter Amount:'))
        c.deposit(amt)
    elif option == 'w' or option == 'W':
        amt = float(input('Enter Amount:'))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        print('Thank you..')
        sys.exit()
    else:
        print('invalid option.. please choose valid option')

