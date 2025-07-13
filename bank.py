from contas import SavingsAccount, CurrentAccount
from pessoas import Client


class Bank:
    def __init__(self, name):
        self._name = name
        self._clients = []
        self._accounts = []

    def add_client(self, client):
        self._clients.append(client)
        self._accounts.append(client.account)

    def authenticate_client(self, client):
        return client in self._clients
    
    def authenticate_account(self, account):
        return account in self._accounts
    
    def verification_process(self, client, value, operation):
        if not isinstance(client, Client):
            raise ValueError('client deve ser da classe Client')
        if not self.authenticate_client(client):
            raise ValueError('Cliente não foi autenticado.')
        if not self.authenticate_account(client.account):
            raise ValueError('Conta não foi autenticada.')
        if not isinstance(value, (int, float)):
            raise ValueError('O valor precisa ser um número.')
        
        if operation == 'withdraw':
            client.withdraw(value)
            print(f'Saque de R${value:.2f} feito com sucesso!')
        elif operation == 'deposit':
            client.deposit(value)
            print(f'Depósito de R${value:.2f} feito com sucesso!')
        else:
            raise ValueError('Operação inválida.')

    def process_withdraw(self, client, value):
        return self.verification_process(client, value, 'withdraw')

    def process_deposit(self, client, value):
        return self.verification_process(client, value, 'deposit')

    def check_balance(self, client):
        if not client in self._clients:
            raise ValueError('O cliente não está autenticado no banco.')
        print(f'O seu saldo é: R${client.account.balance:.2f}')
