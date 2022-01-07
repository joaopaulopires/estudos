print('\33[7;30m{} TABUADA GERAL {}\33[m'.format('X'*20, 'X'*20))
n = int(input('\33[4;36m Escolha um número: \33[m'))
for c in range(0,11):
    x = n*c
    print('\33[1;31m{} X {:2} = \33[1;36m{}\33[m'.format(n, c, x))
print(' ')
print('\33[7;30mX\33[m'*55)