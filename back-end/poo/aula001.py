class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor} realizado com sucesso! Seu saldo agora é R${self.saldo}")
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso! Seu saldo agora é R$ {self.saldo}")
        else:
            print(f'Saldo inssuficiente para saque de R${valor}')

c1 = ContaBancaria("Bruno", 100)
c1.depositar(200)
c1.sacar(120)