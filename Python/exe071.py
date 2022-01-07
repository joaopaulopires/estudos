print('\33[4;32m \33[m'*40)
print('\33[4;32m$\33[m'*40)
print('\33[4;32m{:^40}\33[m'.format(' BANCO PIRES '))
print('\33[4;32m$\33[m'*40)
print(' ')
saque = int(input('\33[4;35mQual valor você quer sacar? R$\33[m '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'\33[1;30mTotal de {totced} cédulas de R${ced}\33[m')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('\33[4;32m \33[m'*40)
print('\33[4;32m$\33[m'*40)
print('\33[1;32mVolte sempre ao BANCO PIRES! Tenha um bom dia !')


