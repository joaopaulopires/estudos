print('\33[31;42m{:^40}\33[m'.format(' MAIOR E MENOR '))
print('{:^50}'.format('\33[31;42m & \33[m'))
print('{:^50}'.format('\33[31;42m MÉDIA \33[m'))
maior = menor = 0
s = c = 0
r = 'S'
while r in 'Ss':
    n = int(input('\33[31;1mDigite um número: \33[m'))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < maior:
            menor = n
    print(' ')
    r = str(input('\33[1;30m Deseja continuar? [S/N] \33[m')).strip().upper()
    print('\33[32m-=\33[m'*20)
print('\33[32m-=\33[m'*20)
print('\33[1;36mA MÉDIA entre os {} números é \33[4;36m {:.2f} \33[m'.format(c, s/c))
print('\33[1;36mO MAIOR número é \33[4;36m {} \33[m'.format(maior))
print('\33[1;36mE o MENOR número é \33[4;36m {} \33[m'.format(menor))
print('\33[32m-=\33[m'*20)