class Account:
    bank_accountant = {'': 0}

    def __init__(self, name='', deposite=1):
        self.name = name
        self.deposite = deposite

    # Добавить новый аккаунт
    def add_new_acc(self):
        Account.bank_accountant[name] = self.deposite
        print(f'Держатель счета: {self.name}')
        print(f'Сумма на счете: ${Account.bank_accountant[name]}')

    # Добавляем к имеющейся сумме на счете новое поступление
    def add_cash(self):
        Account.bank_accountant[name] += self.deposite
        print(f'Вы внесли ${self.deposite} \nОстаток на счете {self.name}: ${Account.bank_accountant[name]}')

    # Снимаем деньги с счета
    def remove_cash(self):
        # предотвращаем ситуацию когда денег можно снять больше чем есть на счете
        if self.deposite < Account.bank_accountant[name]:
            Account.bank_accountant[name] -= self.deposite
            print(f'Вы сняли ${self.deposite} \nОстаток на счете {self.name}: ${Account.bank_accountant[name]}')
        else:
            print('Операция не может быть выполнена. На счете недостаточно средств.')

    # Закрываем счет
    def remove_account(self):
        print(f'Вы сняли ${Account.bank_accountant[name]}')
        Account.bank_accountant.pop(name)
        print(f'Счет на имя {self.name} закрыт')

    # вызываем список достпуных имен
    def available_acc(self):
        print('| '.join(Account.bank_accountant.keys()))

    # Уточняем остаток на счете
    def available_balance(self):
        print(f'Остаток на счете {self.name}: ${Account.bank_accountant[name]}')


while True:
    a = int(input('Пожалуйста выберить оперцию которую хотите выполнить. Просто введите номер операции.\n'
                  '1. Открыть новый счет.\n'
                  '2. Внести деньги на счет.\n'
                  '3. Снять деньги с счета.\n'
                  '4. Закрыть счет.\n'
                  '5. Узнать доступный остаток на счете.'))
    if a == 1:
        name = input('Введите свое имя: ')
        deposite = int(input('Введите сумму которую вы хотите внести на депозит: $'))
        account = Account(name, deposite)
        account.add_new_acc()
        continue
    elif a == 2:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Введите свое имя: ')
        deposite = int(input('Введите сумму которую вы хотите внести на депозит: $'))
        account = Account(name, deposite)
        account.add_cash()
        continue
    elif a == 3:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Введите свое имя: ')
        deposite = int(input('Введите сумму которую вы хотите снять с депозита: $'))
        account = Account(name, deposite)
        account.remove_cash()
        continue
    elif a == 4:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Введите свое имя: ')
        account = Account(name, deposite)
        account.remove_account()
        continue
    elif a == 5:
        account = Account(name, deposite)
        account.available_acc()
        name = input('Введите свое имя: ')
        account = Account(name, deposite)
        account.available_balance()
