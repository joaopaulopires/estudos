print('\33[4;31m+\33[m'*40)
print('\33[1;31m{:^40}\33[m'.format(' CADASTRO '))
print('\33[4;31m+\33[m'*40)
print(' ')
c = c2 = c3 = 0
while True:
    idade = int(input('\33[1;36mQual a sua idade? \33[m'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\33[1;35mQual o seu sexo? [M/F] \33[m')).strip().upper()[0]
    if idade > 18:
        c += 1
    if sexo in 'M':
        c2 += 1
    if sexo == 'F' and idade < 20:
        c3 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('\33[1;30mQuer continuar? [S/N] \33[m')).strip().upper()
    if r == 'N':
        break
    print('\33[1;31m-\33[m'*40)
print('\33[1;31m=\33[m'*40)
print(f'\33[4;31m {c} pessoas \33[1;31m têm mais de 18 anos\33[m')
print(f'\33[1;35mForam cadastrados \33[4;35m {c2} homens \33[1;35m e \33[4;36m {c3} mulheres \33[1;36mcom menos de 18 anos.\33[m')