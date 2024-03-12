# Classes são modelos que definem como os objetos devem ser criados.

class Pessoa:
    
    # O construtor da classe Pessoa recebe os atributos nome e idade
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
