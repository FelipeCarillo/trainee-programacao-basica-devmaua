# Exemplo 1: Loop com for para iterar sobre uma lista
print("\nExemplo 1: Loop com for para iterar sobre uma lista\n")
frutas = ['maçã', 'banana', 'uva', 'morango']
for fruta in frutas:
    print(fruta)

# ou
print()
for i in range(len(frutas)): # len(frutas) retorna o número de elementos na lista frutas
    print(frutas[i])

# Exemplo 2: Loop com for para gerar uma sequência numérica
print("\nExemplo 2: Loop com for para gerar uma sequência numérica\n")
for i in range(1, 6): # range(1, 6) gera uma sequência de 1 a 5 (6 não incluso)
    print(i)

# Exemplo 3: Loop com while para contar até 5
print("\nExemplo 3: Loop com while para contar até 5\n")
contador = 1
while contador <= 5: # enquanto contador for menor ou igual a 5
    print(contador)
    contador += 1

# Exemplo 4: Loop com while e break para encontrar o primeiro número par em uma sequência
print("\nExemplo 4: Loop com while e break para encontrar o primeiro número par em uma sequência\n")
numero = 1
while True: 
    if numero % 2 == 0: 
        print(f'O primeiro número par é: {numero}')
        break
    numero += 1

# Exemplo 5: Loop com for e continue para pular números ímpares
print("\nExemplo 5: Loop com for e continue para pular números ímpares\n")
for i in range(1, 11): # range(1, 11) gera uma sequência de 1 a 10
    if i % 2 != 0:
        continue
    print(i)

# Exemplo 6: Loop com for e else para verificar se há um item específico em uma lista
print("\nExemplo 6: Loop com for e else para verificar se há um item específico em uma lista\n")
animais = ['cachorro', 'gato', 'peixe', 'pássaro']
animal_procurado = 'gato'
for animal in animais: 
    if animal == animal_procurado:
        print(f'{animal_procurado} encontrado!')
        break
else:
    print(f'{animal_procurado} não encontrado na lista.')

# Exemplo 7: Nested loops (loops aninhados)
print("\nExemplo 7: Nested loops (loops aninhados)\n")
for i in range(1, 4): 
    for j in range(1, 4):
        print(f'({i}, {j})')

# Exemplo 8: Usando enumerate para obter índice e valor em um loop
print("\nExemplo 8: Usando enumerate para obter índice e valor em um loop\n")
frutas = ['maçã', 'banana', 'uva', 'morango']
for indice, fruta in enumerate(frutas):
    print(f'Índice {indice}: {fruta}')
