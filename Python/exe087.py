print('{: ^30}'.format(' MATRIZ (versão 2)'))
print('-='*15)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valor = 0
somapar = 0
somacol = 0
c = 0
for lista in matriz:
    for i in range(0, 3):
        valor = int(input(f'Digite um valor para [{matriz.index(lista)}, {i}]'))
        lista[i] = valor
print('-='*15)
for lista in matriz:
    for unidade in lista:
        print(f'[ {unidade: ^4} ]', end=' ')
        if unidade % 2 == 0:
            somapar += unidade
        if unidade == lista[2]:
            somacol += unidade
    print()
print('-='*15)
for lista in matriz:
    for unidade in lista:
        if lista == matriz[1]:
            if c == 0:
                maior = lista[0]
            elif maior < unidade:
                maior = unidade
            c += 1

print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da 3ª coluna é {somacol}')
print(f'O maior valor na 2ª linha é {maior}')
