from time import sleep
print('\33[30;46m{}{}{}\33[m'.format('*'*20, ' CÁLCULO ', '*'*20))
print('\33[4;36m*\33[m'*49)
opcao = 0
n1 = int(input('\33[4;30mDigite o 1º valor:\33[m '))
n2 = int(input('\33[4;30mDigite o 2º valor:\33[m '))
while opcao != 5:
    print('\33[30;45m[1] SOMAR           \33[m')
    print('\33[30;44m[2] MULTIPLICAR     \33[m')
    print('\33[30;42m[3] NOVOS NUMEROS   \33[m')
    print('\33[30;41m[4] MAIOR VALOR     \33[m')
    print('\33[30;43m[5] SAIR DO PROGRAMA\33[m')
    opcao = int(input('\33[30;4mEscolha a opção:\33[m '))
    if opcao == 1:
        n3 = n1 + n2
        print('\33[30;45mA SOMA entre {} + {} é igual a {}.\33[m'.format(n1, n2, n3))
    elif opcao == 2:
        n3 = n1 * n2
        print('\33[30;44mA MULTIPLICAÇÃO entre {} x {} é igual a {}.\33[m'.format(n1, n2, n3))
    elif opcao == 3:
        n1 = int(input('\33[4;30mDigite o 1º valor:\33[m '))
        n2 = int(input('\33[4;30mDigite o 2º valor:\33[m '))
    elif opcao == 4:
        if n1 < n2:
            maior = n2
        else:
            maior = n1
        print('\33[30;41m{} é o maior valor digitado\33[m'.format(maior))
    elif opcao == 5:
        print('\33[1;30mFINALIZANDO...\33[m')
    else:
        print('\33[7;30m OPÇÃO INVÁLIDA \33[m')
    print('\33[36m-=\33[m' * 25)
    print(' ')
    sleep(2)
print('\33[30;43mFIM DO PROGRAMA\33[m')
