print('\33[4;30;43m{}{}{}\33[m'.format('<='*15, ' LOJA DE FERRAMENTAS JOTA ', '=>'*15))
print(' ')
preço = float(input('\33[33;1mVALOR TOTAL DA COMPRA:\33[m '))
print('\33[7;30m FORMAS DE PAGAMENTO:\33[m')
print('\33[4;30;41m [ 1 ] \33[m \33[31;1mÀ vista dinheiro/cheque: \33[30;4mdesconto de 10%\33[m')
print('\33[4;30;42m [ 2 ] \33[m \33[32;1mÀ vista no cartão: \33[4;30m5% de desconto\33[m')
print('\33[4;30;45m [ 3 ] \33[m \33[35;1mEm até 2x no cartão: \33[4;30mpreço normal\33[m')
print('\33[4;44;30m [ 4 ] \33[m \33[34;1mEm 3x ou mais no cartão: \33[4;30m20% de juros\33[m')
modalidade = int(input('\33[33;1mESCOLHA SUA OPÇÃO:\33[m'))

if modalidade ==1:
    total = preço - (preço/100*10)
    print('\33[4;31mO valor final da sua compra, com 10% de desconto, será \33[4;30;41mR${:.2f}\33[m'.format(total))
elif modalidade == 2:
    total = preço - (preço/100*5)
    print('\33[4;32mO valor da sua compra, com 5% de desconto, será \33[4;30;42mR${:.2f}\33[m'.format(total))
elif modalidade == 3:
    print('\33[4;35mNessa condição não há desconto, o valor de sua compra permanece \33[4;30;45mR${:.2f}\33[m'.format(preço))
elif modalidade == 4:
    parcela = int(input('\33[1;33mEm quantas vezes?\33[m'))
    total = preço + (preço/100*20)
    totparcela = total/ parcela
    print('\33[4;34mO valor da sua compra, com acréscimo de 20%, será {}x de R${:.2f} totalizando \33[4;30;44mR${:.2f}\33[m'.format(parcela, totparcela, total))
else:
    print('OPÇÃO INVÁLIDA')
print(' ')
print('\33[4;30;43m{}{}{}\33[m'.format('<='*15, ' VOLTE SEMPRE! ', '=>'*15))