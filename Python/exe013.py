print('')
print('{:$^60}'.format(' CALCULE O REAJUSTE DO SEU SALÁRIO! '))
s = float(input('Quanto você recebe? R$ '))
p = float(input('% = '))
r = s+(s/100)*p
print('Seu salário foi reajustado em {}%, \nPortanto você passará a receber R$ {:.2f}'.format(p, r))
