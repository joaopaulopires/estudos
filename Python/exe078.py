#versãojão
print('\33[4;30;45m{:^40}\33[m'.format(' ANÁLISE DE LISTAS'))
n = list()
for cont in range(0, 5):
    n.append(int(input('\33[1;30mDigite um valor:\33[m ')))
print('\33[1;35mOs valores digitados foram: \33[m', end='')
for c in n:
    print(f'\33[4;35m{c}\33[m', end='\33[4;35m \33[m')
print(f'\n\33[1;34mO maior valor digitado foi \33[4;34m{max(n)} \33[1;34mnas posições \33[m', end='')
for cont in range(0, len(n)):
    if max(n) == n[cont]:
        print(f'\33[4;34m{cont}... \33[m', end='')
print(f'\n\33[1;33mO menor valor digitado foi \33[4;33m{min(n)} \33[1;33mnas posições \33[m', end='')
for val in range(0, len(n)):
    if min(n) == n[val]:
        print(f'\33[4;33m{val}... \33[m', end='')
print(' ')
print('Versão Guanabara')
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if maior < listanum[c]:
            maior = listanum[c]
        elif menor > listanum[c]:
            menor = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior}  nas posições', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f' {i}...', end=' ')
print(f'\nO menor valor digitado foi {menor}  nas posições', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f' {i}...', end=' ')

