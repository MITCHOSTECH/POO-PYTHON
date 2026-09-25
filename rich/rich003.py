from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preço")

tabela.add_column("Nome", justify="right", style="red") # criar coluna (Nome) alinhada á direita
tabela.add_column("Preço", justify="center", style="blue")# Criar coluna (Preço) centralizada

tabela.add_row("Lápis", "1,50€")
tabela.add_row("Borracha", "[green]5,00€[/]")

print(tabela)