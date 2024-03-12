# Exemplo de variável numérica
# As variáveis numéricas podem ser de 2 tipos: int e float
idade = 25
altura = 1.75

# Exemplo de variável de texto (string)
# As strings são imutáveis, ou seja, não podem ser alteradas
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome # Concatenação
nome_completo = f"{nome} {sobrenome}" # Interpolação
nome_completo = "{} {}".format(nome, sobrenome) # Método format

# Exemplo de variável booleana
# As variáveis booleanas podem assumir apenas dois valores: True ou False
ativo = True
aprovado = False

# Exemplo de variável de lista
# As listas sãTo mutáveis, ou seja, podem ser alteradas
numeros = [1, 2, 3, 4, 5]
numeros[0] # Output: 1
numeros[1] # Output: 2
numeros[2] # Output: 3
numeros[3] # Output: 4
numeros[4] # Output: 5

nomes = ["Maria", "Pedro", "Ana"]
nomes[0] # Output: "Maria"
nomes[1] # Output: "Pedro"
nomes[2] # Output: "Ana"

# Exemplo de variável de dicionário
# Os dicionários são compostos por pares de chave e valor
pessoa = {
    "nome": "João",
    "idade": 25,
    "altura": 1.75
}

pessoa["nome"] # Output: "João"
pessoa["idade"] # Output: 25
pessoa["altura"] # Output: 1.75

# Exemplo de variável de tupla
# As tuplas são imutáveis, ou seja, não podem ser alteradas
coordenadas = (10, 20)

# Exemplo de variável de conjunto
# Os conjuntos não permitem elementos duplicados
cores = {"vermelho", "azul", "verde"}

# Exemplo de variável nula
# A variável nula é aquela que não possui valor
valor = None

# Exemplo de conversão de variável numérica para string
numero = 10
numero_em_texto = str(numero)

# Exemplo de conversão de variável de texto para numérica
texto = "100"
texto_em_numero = int(texto)