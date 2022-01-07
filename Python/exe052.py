print('\33[4;30;41m{}{}{}\33[m'.format('-='*10, ' NÚMERO PRIMO ', '-='*10))
n = int(input('\33[4;32mDigite um número:\33[m '))
divisivel = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\33[33m', end='')
        divisivel += 1
    else:
        print('\33[31m', end='')
    print('{}\33[m '.format(c), end='')
print('\n\33[34mO número \33[30;44m {} \33[34m foi divisível \33[33m{}\33[34m vezes'.format(n, divisivel))
if divisivel == 2:
    print('\33[1;32mPortanto, ele é um \33[4;30;41m NÚMERO PRIMO \33[m')
else:
    print('\33[31mPortanto, ele não é um NÚMERO PRIMO.')
print('\33[31m-=\33[m'*30)