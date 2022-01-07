print('\33[4;35m{:^40}\33[m'.format(' ANÁLISE DE LISTAS II'))
valor =[]
while True:
    cont = 0
    valor.append(int(input('\33[1;30mDigite um valor: \33[m')))
    for num in valor:
        if valor.count(num) == 2:
            valor.pop()
            cont = 1
    if cont == 1:
        print('\33[1;31mValor duplicado! Não vou adicionar...\33[m')
    else:
        print('\33[1;34mValor adicionado com sucesso!\33[m')
    r = ' '
    while r not in 'SN':
        r = str(input('\33[1;30mQuer continuar? [S/N] \33[m')).strip().upper()[0]
    if r in 'N':
        break
    print('\33[1;35m-\33[m'*20)
print('\33[1;35m=\33[m'*20)
valor.sort()
print(f'\33[1;36mVocê digitou os valores \33[4;36m{valor}\33[m')
print(' ')


print('Versão guanabara')
números = []
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('\33[1;34mValor adicionado com sucesso!\33[m')
    else:
        print('\33[1;31mValor duplicado! Não vou adicionar...\33[m')
    r = str(input('\33[1;30mQuer continuar? [S/N] \33[m')).strip().upper()[0]
    if r in 'N':
        break
valor.sort()
print(f'\33[1;36mVocê digitou os valores \33[4;36m{números}\33[m')