r = ' '
while r != 'N':
    print('\33[30;47m{} {} {}\33[m'.format('X'*20, 'CÁLCULO DE FATORIAL', 'X'*20))
    print(' ')
    n = int(input('\33[4;35m Digite o fatorial: \33[m'))
    print('\33[1;31m{}! \33[1;32m= {} \33[m'.format(n, n), end='')
    c = n - 1
    while c != 0:
        if c > 0:
            if c == n-1:
                f = n * c
                print('\33[1;32mX {} \33[m'.format(c), end='')
            else:
                print('\33[1;32mX {} \33[m'.format(c), end='')
                f = f * c
            c = c -1
    print('\33[1;32m = \33[4;31m{}\33[m'.format(f))
    print(' ')
    r = str(input('\33[1;30m Deseja calcular outro fatorial? [S/N] \33[m')).upper()
    print(' ')
print('\33[30;47;1m FIM \33[m')