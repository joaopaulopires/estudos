print('\33[30;42m{}{}{}\33[m'.format('>'*20, ' SEQUÊNCIA DE FIBONACCI ', '<'*20))
print('\33[1;32m-\33[m'*50)
n1 = 0
n2 = 1
c = 2
n = int(input('\33[1;32mQuantos números você quer ver na \33[4;32m Sequencia de Fibonacci? \33[m '))
print('\33[31;1m{}, {}, '.format(n1, n2), end= '')
while c != n:
    n3 = n1 +n2
    print('\33[31;1m{},\33[m '.format(n3), end='')
    n1 = n2
    n2 = n3
    c += 1
print('\33[7;30m FIM \33[m')