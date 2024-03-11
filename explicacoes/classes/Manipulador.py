from Aluno import Aluno
from Pessoa import Pessoa

# Criando uma instância da classe Pessoa, um objeto da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Acessando atributos da instância
print(f"Nome: {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")

# Mudando o valor do atributo da instância
pessoa1.nome = "José"
print(f"\nNome: {pessoa1.nome}")

# Chamando um método da instância
mensagem_de_cumprimento = pessoa1.cumprimentar()
print(mensagem_de_cumprimento)

# Criando uma instância da classe Aluno, um objeto da classe Aluno
aluno = Aluno("Maria", 20, "12345")

# Acessando atributos da instância
print(f"\nNome: {aluno.nome}")
print(f"Idade: {aluno.idade}")
print(f"Matrícula: {aluno.matricula}")

# Mudando o valor do atributo da instância
aluno.nome = "Mariana"
print(f"\nNome: {aluno.nome}")

# Chamando os métodos da instância
mensagem_de_cumprimento = aluno.cumprimentar()
print(mensagem_de_cumprimento)

mensagem_de_estudo = aluno.estudar()
print(mensagem_de_estudo)