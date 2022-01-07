def area(larg, comp):
    resultado = larg * comp
    print('-'*26)
    print(f'{"CONTROLE DE TERRENOS":^26}')
    print('-'*26)
    print(f'LARGURA (m): {larg}')
    print(f'COMPRIMENTO (m): {comp}')
    print(f'A área de um terreno {larg} x {comp} é de {resultado}m².')


print('\33[4;30m Digite as medidas do terreno: \33[m')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)