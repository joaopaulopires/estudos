listagem = ('rodo', 19.9,
            'TV', 798.67,
            'camisa', 38,
            'isqueiro', 4.5,
            'mamadeira', 12.5)
print('='*50)
print('{:^50}'.format( ' LISTAGEM DE PREÇOS '))
print('='*50)
for compra in listagem:
    if listagem.index(compra)% 2 == 0:
        print(f'{compra:.<40}', end='')
    else:
        print(f'R$ {compra:>6.2f}')
print('='*50)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<40}', end='')
    else:
        print(f'R$ {listagem[c]:>6.2f}')
print('='*50)