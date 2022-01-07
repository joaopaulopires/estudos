from random import randint
from time import sleep
def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        números.append(randint(0, 100))
        print(números[c], end=' ')
        sleep(0.5)
    print()
def somaPar():
    soma = 0
    for c in números:
        if c % 2 == 0:
            soma += c
    if soma > 0:
        print(f'A soma dos números pares é {soma}')
    else:
        print('Não foram sorteados números pares.')



números = list()
sorteia()
somaPar()