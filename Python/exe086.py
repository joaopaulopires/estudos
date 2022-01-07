print('{: ^30}'.format(' MATRIZ (versão 2)'))
print('-='*15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = 0
for lista in matriz:
    for i in range(0, 3):
        valor = int(input(f'Digite um valor para [{matriz.index(lista)}, {i}]'))
        lista[i] = valor
print('-='*15)
for lista in matriz:
    for unidade in lista:
        print(f'[ {unidade: ^4} ]', end=' ')
    print()
'''print('-='*30)
print('{: ^30}'.format(' MATRIZ (guanabara)'))
print('-='*15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = 0
for l in range(0, len(matriz)):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
print('-='*15)
for l in range(0, len(matriz)):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]: ^4} ]', end=' ')
    print()'''
'''versão 1
matriz = [[[], [], []], [[], [], []], [[], [], []]]
valor = 0
for l, lista in enumerate(matriz):
    for i, unidade in enumerate(lista):
        valor = int(input(f'Digite um valor para [{l}, {i}]'))
        matriz[l][i].append(valor)
print('-='*20)
print(f'{}')
for lista in matriz:
    print('\n')
    for unidade in lista:
        print(f'{unidade}', end=' ')'''