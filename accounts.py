from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self._agency = agency
        self._account = account
        self._balance = balance

    @property
    def agency(self):
        return self._agency
    @property
    def account(self):
        return self._account
    @property
    def balance(self):
        return self._balance
    
    @abstractmethod
    def withdraw(self, value): ...

    def details(self, msg = ''):
        print(f'O seu saldo é: R${self._balance:.2f} | {msg}')
        
    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Utilize números válidos para o depósito.')
        elif value < 0:
            raise ValueError('Não é possível depositar um valor negativo.')
        else:
            self._balance += value
            self.details(f'Depositado: R${value:.2f}')


class SavingsAccount(Account):
    def withdraw(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Use apenas números para fazer o saque.')
        elif value > self._balance:
            raise ValueError('O valor de saque deve ser menor ou igual ao saldo.')
        else:
            self._balance -= value
            self.details(f'Sacado: R${value:.2f}')


class CurrentAccount(Account):
    def __init__(self, agency, account, balance, limit = 0):
        super().__init__(agency, account, balance)
        self._limit = limit
    
    def withdraw(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Use apenas números para fazer o saque.')
        elif self._balance + self._limit < value:
            raise ValueError('Não será possível sacar esse valor.')
        else:
            self._balance -= value
            self.details(f'Sacado: R${value:.2f}')
