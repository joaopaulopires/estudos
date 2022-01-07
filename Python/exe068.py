from random import randint
from time import sleep
print('\33[4;33m¨\33[m'*40)
print('\33[4;33m{:^40}'.format(' PAR OU IMPAR '))
print('\33[4;33m¨\33[m'*40)
c = 0
print('\33[4;31m VAMOS JOGAR? \33[m')
while True:
    jogador = int(input('\33[1;33mDigite um valor:\33[m '))
    while True:
        pi = str(input('\33[1;34mPar ou Impar? [P/I]\33[m ')).strip().upper()[0]
        if pi in 'PI':
            break
    #SOLUÇÃO CURSO#
    #pi = ' '
    #while pi not in 'PI':
        #pi = str(input('\33[1;34mPar ou Impar? [P/I]\33[m ')).strip().upper()[0]
    computador = randint(0, 50)
    total = jogador + computador
    print('\33[7;30m ESPERE... \33[m')
    sleep(0.5)
    print(f'\33[1;33m O computador jogou {computador} e a soma deu {total} \33[m')
    print('\33[1;34mÉ PAR!\33[m' if total%2==0 else '\33[1;31mÉ ÍMPAR!\33[m')
    if pi == 'P':
        if total % 2 == 0:
            c += 1
            print(f'\33[4;30;41m Você ganhou!!! {total} é PAR. \33[m')
        else:
            break
    if pi == 'I':
        if total % 2 == 0:
            break
        else:
            c += 1
            print(f'\33[4;30;43m Você ganhou! {total} é ÍMPAR. \33[m')
    print('\33[1;33m=\33[m'*40)
print('\33[4;33m¨\33[m'*40)
if c == 1:
    print(f'\33[1;31m Agora você perdeu... \33[4;30;41m mas acertou {c} vez \33[m')
else:
    print(f'\33[1;31m Agora você perdeu... \33[4;30;41m mas acertou {c} vezes \33[m')
