class Customer:
    bank_name = 'Imperial Bank'

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print('After deposit your current balance is ', self.balance)

    def withdrawal(self, amount):
        if amount > self.balance:
            print('Sorry! Insufficient funds..')
        else:
            self.balance = self.balance - amount
            print('After withdrawal your current balance is ', self.balance)



name = input('Please enter your name: ')
print('Hello',name,'! Welcome to',Customer.bank_name)
c = Customer(name)
while True:
    print('d for Deposit \nw for withdrawal \ne for exit')
    option = input('Please enter the keyword for our services: ')
    if option.lower() == 'd':
        amount = float(input('Enter the amount to deposit: '))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter the amount to withdraw: '))
        c.withdrawal(amount)
    elif option.lower() == 'e':
        print('Thankyou for banking with us!')
        break
    else:
        print('Please choose correct keyword..')
