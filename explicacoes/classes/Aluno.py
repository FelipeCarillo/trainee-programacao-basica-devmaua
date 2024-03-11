from Pessoa import Pessoa

# Criando a classe filha Aluno
class Aluno(Pessoa):
    
    # O construtor da classe filha Aluno recebe os atributos nome, idade e matrícula
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade) # Chamando o método __init__ da classe mãe (Pessoa) para inicializar os atributos herdados
        self.matricula = matricula # Atributo específico da classe Aluno

    def estudar(self):
        return f"{self.nome} está estudando."
