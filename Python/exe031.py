print('{:#^50}'.format(' LOCADORA DE VEÍCULOS JÃO '))
print('-=-' * 25)
km = int(input('Qual a distância da sua viagem? '))
if km <= 200:
    tot1 = km*0.5
    print('Distância percorrida: {}km \nValor por km rodado: R$0,50 \nValor total: R${:.2f}'.format(km, tot1))
else:
    tot2 = km*0.45
    print('Distância percorrida: {}km \nValor por km rodado: R$0,45 \nValor total: R${:.2f}'.format(km, tot2))
print('-=-'*25)
print('A Locadora de Veículos Jão deseja à você uma boa viagem!')