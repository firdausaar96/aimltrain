class Account:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print('Balance after deposit: ',self.balance)
    
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
            print('Balance after withdraw: ',self.balance)
        else:
            print('Insufficient amount in the account: ')
            print('Transaction failed!!!!!')

    def display(self):
        print(f'Account Holder Name: {self.holder} \nAccount Balance: {self.balance}')

ac=Account("Sam",15000)
ac.display()
choose=print(int(input('Please choose \n1.Deposit \n2.Withdraw\n')))

if(choose==1):
    damount=float(input('Enter amount to deposit: '))
    ac.deposit(damount)
elif(choose==2):
    damount=float(input('Enter amount to withdraw: '))
    ac.withdraw(damount)
else:
    print('Wrong choice')
