listagem = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        listagem[0].append(n)
    else:
        listagem[1].append(n)
print(listagem)
listagem[0].sort()
listagem[1].sort()
print(f'Os valores pares digitados foram: {listagem[0]}')
print(f'Os valores ímpares digitados foram: {listagem[1]}')
