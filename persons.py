from contas import SavingsAccount, CurrentAccount


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

        if not isinstance(age, int):
            raise ValueError('A idade deve ser um número inteiro.')

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age


class Client(Person):
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self._account = account

        if not isinstance(account, (SavingsAccount, CurrentAccount)):
            raise ValueError('A conta deve ser ou SavingsAccount ou CurrentAccount.')
        
    @property
    def account(self):
        return self._account

    def deposit(self, value):
        return self._account.deposit(value)

    def withdraw(self, value):
        return self._account.withdraw(value)
    
    def check_balance(self):
        print(f'O seu saldo é: R${self._account.balance:.2f}')
