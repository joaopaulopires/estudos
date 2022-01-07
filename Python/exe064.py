print('\33[7;30m{}{}{}\33[m'.format('#'*15, ' TESTE DE FLAG ','#'*15))
print('{:^55}'.format('\33[7;30m CONDIÇÃO DE PARADA \33[m'))
n = c = s = 0
while n != 999:
    n = int(input('\33[1;31mDigite um número: \33[m'))
    if n != 999:
        c += 1
        s += n
print('\33[1;34mForam digitados \33[4;34m{} números.\33[1;34m E a SOMA entre eles é \33[4;34m{}\33[m'.format(c, s))