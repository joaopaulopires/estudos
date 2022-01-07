def aumentar(n=0, taxa=0, sit=False):
    res = (n + (n / 100) * taxa)
    return res if sit is False else moeda(res)


def diminuir(n=0, taxa=0, sit=False):
    res = n - (n / 100) * taxa
    return res if sit is False else moeda(res)


def dobro(n, sit=False):
    res = n * 2
    return res if sit is False else moeda(res)


def metade(n=0, sit=False):
    res = n / 2
    return res if not sit else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def resumo(n, taxaa=0, taxar=0):
    print('-'*30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço:\t\t{dobro(n, True)}')
    print(f'Metade do preço:\t{metade(n, True)}')
    print(f'{taxaa}% de aumento:\t{aumentar(n, taxaa, True)}')
    print(f'{taxar}% de redução:\t{diminuir(n, taxar, True)}')
    print('-'*30)
