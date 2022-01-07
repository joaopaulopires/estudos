print('\33[4;32m{:^40}\33[m'.format(' LISTAS PARES E ÍMPARES'))
num = []
par = []
impar = []
while True:
    num.append(int(input('\33[1;34mDigite uma valor: \33[m')))
    r = ' '
    while r not in 'SN':
        r = str(input('\33[1;30mDeseja continuar? [S/N] \33[m')).strip().upper()[0]
    if r == 'N':
        break
    print('-'*30)
print('='*30)
print(f'\33[1;32mA lista completa é \33[4;32m{num}\33[m')
for valor in num:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'\33[1;34mA lista de pares é \33[4;34m{par}\33[m')
print(f'\33[1;35mA lista de ímpares é \33[4;35m{impar}\33[m')
