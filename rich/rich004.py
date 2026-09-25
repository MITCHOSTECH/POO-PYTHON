from rich import print
from rich import inspect
'''print(int.__doc__)# informação sobre inte de forma normal
print(int.__dict__)# '' ''   de forma disperça
inspect(int, all=True) # Informação com precisão avançadas e organizada

'''
class ContaBancaria:
    """
Cria uma conta bancária  que permite fazer saques e dépositos
    """
    def __init__(self, id, nome, dinheiro = 0):# Metodo construtor
        self.id = id
        self.titular = nome
        self.saldo = dinheiro
        print(f"Conta {self.id} criada com sucesso. Com Saldo atual de {self.saldo:,.2f}€")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem €{self.saldo:,.2f} de saldo"

    def depositar(self, valor):
        self.saldo += valor
        print(f"Déposito de €{valor:,.2f} autorizado na conta {self.id}")

    def saquar(self, valor):
        if valor > self.saldo:
            print(f"\033[31mSaque negado de {valor:,.2f}€ na conta {self.id} saldo INSUFICIÊNTE!\033[m")
        else:
            self.saldo -= valor
            print(f"Saque de {valor:,.2f} autorizado na conta:{self.id}")




c = ContaBancaria(112, "Ricardo", 3000)
#inspect(c) # Serve para melhor visualização dos dados em forma de painel
print(c.__getstate__())# Serve para mostrar dados de maneira melhor em forma de dicionário