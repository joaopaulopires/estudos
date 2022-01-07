print('\33[4;32m{:^40}\33[m'.format(' ANÁLISE DE LISTAS VARIADAS'))
valor = []
while True:
    valor.append(int(input('\33[1;32mDigite um valor: \33[m')))
    r = ' '
    while r not in 'SN':
        r = str(input('\33[1;30mDeseja continuar? [S/N] \33[m')).strip().upper()[0]
    if r == 'N':
        break
    print('\33[1;32m-\33[m'*30)
print(f'\33[1;33mForam digitados {len(valor)} valores.\33[m')
valor.sort(reverse=True)
print(f'\33[1;34mO valores em ordem descrecente: {valor}\33[m')
if 5 in valor:
    print('\33[1;33mO valor 5 faz parte da lista.')
else:
    print('\33[1;31mO valor 5 não faz parte da lista.\33[m')

