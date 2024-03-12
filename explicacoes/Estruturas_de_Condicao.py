# Exemplo 1: Uso simples do if-else
print("\nExemplo 1: Uso simples do if-else\n")
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo 2: Uso de elif para várias condições
print("\nExemplo 2: Uso de elif para várias condições\n")
nota = 75
if nota >= 90:
    print("A")
elif 80 <= nota < 90:
    print("B")
elif 70 <= nota < 80:
    print("C")
else:
    print("F")

# Exemplo 3: Verificação de par ou ímpar
print("\nExemplo 3: Verificação de par ou ímpar\n")
numero = 7
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

# Exemplo 4: Verificação se um número está dentro de um intervalo
print("\nExemplo 4: Verificação se um número está dentro de um intervalo\n")
numero = 25
if 20 <= numero <= 30:
    print(f"{numero} está dentro do intervalo de 20 a 30.")
else:
    print(f"{numero} está fora do intervalo de 20 a 30.")

# Exemplo 5: Uso de operador ternário
print("\nExemplo 5: Uso de operador ternário\n")
idade = 22
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)

# Exemplo 6: Uso de operadores lógicos
print("\nExemplo 6: Uso de operadores lógicos\n")
tem_carteira = True
tem_idade = 21

if tem_carteira and tem_idade >= 18:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")

# Exemplo 7: Uso de operadores lógicos com strings
print("\nExemplo 7: Uso de operadores lógicos com strings\n")
usuario_autenticado = True
tem_permissao = True

if usuario_autenticado or tem_permissao:
    print("Acesso permitido.")
else:
    print("Acesso negado.")

# Exemplo 8: Uso de operadores lógicos com listas
print("\nExemplo 8: Uso de operadores lógicos com listas\n")
numeros = [1, 2, 3, 4, 5]
tem_3 = 3 in numeros
tem_6 = 6 in numeros

if tem_3 and not tem_6:
    print("A lista contém o número 3, mas não contém o número 6.")
else:
    print("A lista não contém o número 3 ou contém o número 6.")
