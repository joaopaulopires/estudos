print('\33[30;46m{}{}{}\33[m'.format('*'*20, ' CÁLCULO ', '*'*20))
print('\33[4;36m*\33[m'*49)
n3 = 0
opcao = 0
while opcao != 4:
    n1 = int(input('\33[4;30mDigite o 1º valor:\33[m '))
    n2 = int(input('\33[4;30mDigite o 2º valor:\33[m '))
    print('\33[30;45m[1] SOMAR           \33[m')
    print('\33[30;44m[2] MULTIPLICAR     \33[m')
    print('\33[30;42m[3] NOVOS NUMEROS   \33[m')
    print('\33[30;43m[4] SAIR DO PROGRAMA\33[m')
    opcao = int(input('\33[30;4mEscolha a opção:\33[m '))
    if opcao != 3:
        if opcao == 1:
            n3 = n1 + n2
            print('\33[30;45mA SOMA entre {} e {} é igual a {}.\33[m'.format(n1, n2, n3))
        if opcao == 2:
            n3 = n1 * n2
            print('\33[30;44mA MULTIPLICAÇÃO entre {} e {} é igual a {}.\33[m'.format(n1, n2, n3))
    print('\33[36m-=\33[m'*25)
print('\33[30;43mFIM\33[m')
