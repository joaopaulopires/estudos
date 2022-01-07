print(''
      '')
n1 = int(input('\33[30mDigite o 1º valor:\33[m '))
n2 = int(input('\33[30mDigite o 2º valor:\33[m '))

if n1>n2:
    print('{} é maior que {} - O \33[4;31m1º valor é maior.\33[m'.format(n1, n2))
elif n1<n2:
    print('{} é maior que {} - O \33[4;31m2º valor é maior.\33[m'.format(n2, n1))
else:
    print('\33[30mNão existe valor maior, os dois são iguais.\33[m')