import emoji
from random import randint
from time import sleep
print('\33[30;45m{}\33[30;42m{}\33[30;46m{}\33[7;30m{}\33[30;45m{}\33[30;42m{}\33[30;46m{}\33[m'.format('#'*5, 'O'*5, 'V'*5, ' JOKENPÔ ', '#'*5, 'O'*5, 'V'*5))
print(' ')
print('\33[4;30;41m PENSE E ... :\33[m')
print(emoji.emojize('\33[30;45m[ 1 ] :fist: PEDRA \33[m', use_aliases=True))
print(emoji.emojize('\33[30;42m[ 2 ] :hand: PAPEL \33[m', use_aliases=True))
print(emoji.emojize('\33[30;46m[ 3 ] :v: TESOURA \33[m', use_aliases=True))
print(' ')
sleep(1)
print(emoji.emojize('\33[1;35m JO :fist: ... \33[m', use_aliases=True))
sleep(1)
print(emoji.emojize('\33[1;32m KEN :hand: ...\33[m', use_aliases=True))
sleep(1)
print(emoji.emojize('\33[1;36m PÔ :v: !\33[m',use_aliases=True))
usuario = int(input('\33[4;30;41m ESCOLHA! \33[m'))
pc = randint(1,3)
if usuario == 1:
    usuario1 = (emoji.emojize('\33[1;35m :fist: \33[m', use_aliases=True))
elif usuario == 2:
    usuario1 = (emoji.emojize('\33[1;32m :hand: \33[m', use_aliases=True))
elif usuario == 3:
    usuario1 = (emoji.emojize('\33[1;36m :v: \33[m',use_aliases=True))
if pc == 1:
    pc1 = (emoji.emojize('\33[1;35m :fist: \33[m', use_aliases=True))
elif pc == 2:
    pc1 = (emoji.emojize('\33[1;32m :hand: \33[m', use_aliases=True))
elif pc == 3:
    pc1 = (emoji.emojize('\33[1;36m :v: \33[m',use_aliases=True))
print('\33[4;31m USUÁRIO \33[m {} \33[4;31m X \33[m {} \33[4;31m PC \33[m'.format(usuario1, pc1))
if usuario == 1 and pc == 2 or usuario == 2 and pc  == 3 or usuario == 3 and pc == 1:
    print('\33[1;31mVOCÊ PERDEU...\33[m')
elif usuario == 1 and pc == 3 or usuario == 2 and pc == 1 or usuario == 3 and pc == 2:
    print('\33[1;31;40m VOCÊ GANHOU!!! PARABÉNS \33[m')
elif usuario == 1 == pc or usuario == 2 == pc or usuario == pc:
    print('\33[1;31m EMPATE! \33[m')
elif usuario >= 4:
    print('\33[30mOPÇÃO INVÁLIDA\33[m')