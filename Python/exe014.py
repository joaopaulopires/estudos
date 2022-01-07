print('{:*^60}'.format(' CONVERSOR DE TEMPERATURA '))

cel = float(input('Digite a temperatura em ºC: '))
far = cel * 1.8 + 32
print('{}ºC equivale a {:.2f}F.'.format(cel, far))
