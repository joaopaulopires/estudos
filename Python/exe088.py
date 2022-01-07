from random import randint
from time import sleep
'''mega = []
print('-'*30)
print('{: ^30}'.format(' MEGA SENA '))
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu sortei? '))
print('{}{}{}{}{}'.format('-='*5, ' SORTEANDO ', jogos,' JOGOS ', '=-'*5))
for c in range(0, jogos):
    mega.append([0, 0, 0, 0, 0, 0])
    for i in range(0, 6):
        n = randint(1, 60)
        if n not in mega:
            mega[c][i] = n
    mega[c].sort()
    sleep(1)
    print(f'Jogo {c+1}: {mega[c]}')
    print()
print('{}{}{}'.format('-=' * 5, '< BOA SORTE! >', '=-' * 5))
print('')'''
print('{:-^30}'.format(' VERSÃO GUANABARA '))
lista = []
mega2 = []
print('-'*30)
print('{: ^30}'.format(' MEGA SENA '))
print('-'*30)
jogos2 = int(input('Quantos jogos você quer que eu sortei? '))
tot = 1
while tot <= jogos2:
    cont = 0
    while True:
        n2 = randint(0, 60)
        if n2 not in lista:
            lista.append(n2)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    mega2.append(lista[:])
    lista.clear()
    tot += 1
print('-='*5, f' SORTEANDO  {jogos2} JOGOS ', '=-'*5)
for i, l in enumerate(mega2):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('FIM')

