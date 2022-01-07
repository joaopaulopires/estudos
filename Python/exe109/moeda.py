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


def resumo(n, jA, jB):
    print('-'*50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-'*50)
    print(f'{"Preço analisado:":<40}R${n}')
    print(f'{"Dobro do preço:":<40}{dobro(n, True)}')
    print(f'{"Metade do preço :":<40}{metade(n, True)}')
    print(f'{jA}{"% de aumento:"}{aumentar(n, taxa, True):>30}')
    print(f'{jB}{"% de redução:"}{diminuir(n, taxa, True):>30}')
    print('-'*50)

