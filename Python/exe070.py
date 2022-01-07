print('\33[4;32m¨\33[m'*40)
print('\33[4;32m{:^40}\33[m'.format(' LOJÃO DO JÃO '))
print('\33[4;32m¨\33[m'*40)
print(' ')
s = c = cont = 0
while True:
    produto = str(input('\33[4;34mNome do Produto:\33[m')).strip()
    preço = float(input('\33[4;33mPreço:\33[m R$'))
    s += preço
    cont += 1
    if preço > 1000:
        c += 1
    if cont == 1 or preçomenor > preço:
        preçomenor = preço
        produtomenor = produto
    #SOLUÇÃO JP#
    # #else:
        #if preçomenor > preço:
            #preçomenor = preço
            #produtomenor = produto
    r = ' '
    while r not in 'SN':
        r = str(input('\33[1;30mQuer continuar? [S/N] \33[m')).strip().upper()[0]
    if r == 'N':
        break
    print('\33[1;36m-\33[m'*40)
print('\33[4;36m¨\33[m'*40)
print(f'\33[1;34mTotal da Compra:\33[4;34m R${s} \33[m')
if c > 1:
    print(f'\33[1;33m{c} produtos\33[1;30m custam mais de \33[1;33mR$1000,00\33[m')
else:
    print(f'\33[1;33m{c} produto\33[1;30m custa mais de \33[1;33mR$1000,00\33[m')
print(f'\33[1;31mO produto mais barato:\33[4;31m {produtomenor} \33[1;31me custa \33[4;31mR${preçomenor}\33[m')