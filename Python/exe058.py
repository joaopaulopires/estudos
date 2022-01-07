from random import randint
from time import sleep
r = ' '
while r != 'N':
    print('\33[1;30;41m{}{}{}\33[m'.format('?'*15, ' ADIVINHE O VALOR! ', '?'*15))
    print('\33[1;32m-\33[m'*45)
    print('\33[4;31m Sou o seu COMPUTADOR!...VAMOS JOGAR? \33[m')
    vc = 11
    c = 0
    pc = randint(0, 10)
    print('\33[1;34mAcabei de pensar em um número de 0 a 10.\nConsegue adivinhar? \33[m')
    while vc != pc:
        vc = int(input('\33[1;34mQual o seu palpite?\33[m '))
        if pc != vc:
            c += 1
            print('\33[1;32mES\33[1;33mPE\33[1;35mRE...\33[m')
            sleep(1)
            if pc < vc:
                print('\33[1;37mÉ menos...Tente mais uma vez!\33[m')
            else:
                print('\33[1;37mÉ mais...Tente mais uma vez!\33[m')
            print(' ')
    if c >1:
        print('\33[1;32mES\33[1;33mPE\33[1;35mRE...\33[m')
        sleep(1)
        print('\33[4;30;41m ACERTOU!!! \33[1;31m E você tentou \33[4;31m {} vezes! \33[m'.format(c))
        print(' ')
    else:
        print('\33[1;32mES\33[1;33mPE\33[1;35mRE...\33[m')
        sleep(1)
        print('\33[4;30;41m ACERTOU!!! \33[1;31m E você tentou apenas \33[4;31m {} vez!!! \33[m'.format(c))
        print(' ')
    r = str(input('\33[30mQuer continuar a jogar? [S/N] \33[m')).strip().upper()[0]
    print('\33[1;32m=\33[m'*45)
print('\33[7;30m FIM DO JOGO! \33[m')

