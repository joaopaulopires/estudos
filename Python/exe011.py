print('{:=^60}'.format(' PINTURA DOMÉSTICA '))
print('')
print('*Para pintar uma parede:')
l = float(input('Largura: '))
al = float(input('Altura: '))
a = l*al
t = a/2
print('Sua parede tem {:.2f}m², então você precisará de {:.2f} litros de tinta.'.format(a, t))

print('*Nossa medida de referência é: 1 litro de tinta = 2m² ')