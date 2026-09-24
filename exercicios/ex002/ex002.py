  #Declaração dde classe

class Gafanhoto:
    """
    Essa classe cria um gaafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessaa, use
    variável = Gafanhoto(nome, idade)
    """
    def __init__(self,n = "Vazio", i = 0): # Método construtor
        # Atributos de Instância
        self.nome = n
        self.idade = i


    # Método de Instancia
    def aniversario(self):
        self.idade += 1

    #def mensagem(self): # É mesmo com def __str__(self)
        #return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


    def __getstate__(self):# Estado de um objeto
        return f"Estado: nome = {self.nome}; idade = {self.idade}"

  #Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
#print(g1.mensagem())# É mesmo com print(g1)

#print(g1.__doc__) # Dunder Attribute # execute a documentação da classe
print(g1)
print(g1.__dict__)# Mostrar os atributos em forma de um dicionário
print(g1.__getstate__())# Mesmo com __dict__ mais é um método, muda conforme o estato de um objeto

#Atualizada
g2 = Gafanhoto("Maauro", 53)
print(g2)

print(g2.__getstate__())# Mostrar estado do objeto

#Saber qual classe pertence um objeto
print(g1.__class__)

"""g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())"""