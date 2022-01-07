from time import sleep
print('\33[1;36;41m{:=^40}\33[m'.format(' BANCO J.P.MORGAN '))
print('{: ^50}'.format('\33[4;36;41m==IMÓVEIS==\33[m'))
nome = str(input('\33[1;31mQUAL O SEU NOME?\33[m ')).upper()
casa = float(input('\33[1;31m{}, INFORME O VALOR DO IMÓVEL EM ANÁLISE:\33[m R$'.format(nome)))
salario = float(input('\33[1;31mCERTO. AGORA INFORME O VALOR DO SEU RENDIMENTO MENSAL:\33[m R$'))
ano = float(input('\33[1;31mEM QUANTOS ANOS VOCÊ PRETENDE PAGAR O IMÓVEL, {}?:\33[m '.format(nome)))
meses = int(ano*12)
prestação = casa/meses
print('\33[7;30mATENÇÃO: o financiamento será autorizado SOMENTE se o valor da prestação for menor que 30% do seu rendimento mensal.\33[m')
sleep(1)
print('\33[1;30mAguarde...\33[m')
sleep(4)
if (salario/100)*30 > prestação:
    print('''\33[30;44mParabéns {}, seu financiamento foi autorizado!\33[m 
    \33[1;30mVocê pagará o seu imóvel em \33[4;30m{} meses\33[m
    \33[30;1mcom parcelas mensais de \33[4;30;41mR${:.2f}\33[m'''.format(nome, meses, prestação))
else:
    print('''\33[1;30mInfelizmente seu rendimento é incompatível com a prestação do imóvel em análise...\33[m
    \33[1;30mMas temos outras opções que contemplam a sua faixa de rendimento. Consulte nosso portal\33[m
    \33[1;30mou fale com um de nossos corretores!\33[m''')

