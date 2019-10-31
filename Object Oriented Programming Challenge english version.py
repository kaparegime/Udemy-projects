class Account:
    bank_accountant = {'': 0}

    def __init__(self, name='', deposite=1):
        self.name = name
        self.deposite = deposite

    # Add new acc
    def add_new_acc(self):
        Account.bank_accountant[name] = self.deposite
        print(f'Account holder: {self.name}')
        print(f'Balance: ${Account.bank_accountant[name]}')

    # Add new money to available acc with money
    def add_cash(self):
        Account.bank_accountant[name] += self.deposite
        print(f'You added ${self.deposite} \nBalance {self.name}: ${Account.bank_accountant[name]}')

    # Get Cash
    def remove_cash(self):
            # Prevent situation then not enough money on balance
        if self.deposite <= Account.bank_accountant[name]:
            Account.bank_accountant[name] -= self.deposite
            print(f'You got ${self.deposite} \nBalance {self.name}: ${Account.bank_accountant[name]}')
        else:
            print('Операция не может быть выполнена. На счете недостаточно средств.')

    # Close acc
    def remove_account(self):
        print(f'You got ${Account.bank_accountant[name]}')
        Account.bank_accountant.pop(name)
        print(f'Account holder {self.name} closed')

    # Call available accs
    def available_acc(self):
        print('| '.join(Account.bank_accountant.keys()))

    # Clerlify available balance
    def available_balance(self):
        print(f'Balance {self.name}: ${Account.bank_accountant[name]}')


while True:
    a = int(input('Please choose the operation you want to perform. Just enter the operation number.\n'
                  '1. Open new account\n'
                  '2. Deposit money into the account.\n'
                  '3. Withdraw money from the account.\n'
                  '4. Close account\n'
                  '5. Available balance.'))
    if a == 1:
        name = input('Enter your name: ')
        deposite = int(input('Enter the amount you want to deposit: $'))
        account = Account(name, deposite)
        account.add_new_acc()
        continue
    elif a == 2:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Enter your name: ')
        deposite = int(input('Enter the amount you want to deposit: $'))
        account = Account(name, deposite)
        account.add_cash()
        continue
    elif a == 3:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Enter your name: ')
        deposite = int(input('Enter the amount you want to withdraw from the deposit: $'))
        account = Account(name, deposite)
        account.remove_cash()
        continue
    elif a == 4:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Enter your name: ')
        account = Account(name, deposite)
        account.remove_account()
        continue
    elif a == 5:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Enter your name: ')
        account = Account(name, deposite)
        account.available_balance()
        continue
    else:
        continue
