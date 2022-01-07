def aumentar(n, taxa=0, sit=False):
    if sit:
        res = moeda(n + (n/100) * taxa)
        return res
    else:
        res = n + (n/100) * taxa
        return res


def diminuir(n, taxa=0, sit=False):
    if sit:
        res = moeda(n - (n / 100) *taxa)
        return res
    else:
        res = n - (n / 100) *taxa
        return res


def dobro(n, sit=False):
    if sit:
        res = moeda(n * 2)
        return res
    else:
        res = n * 2
        return res


def metade(n, sit=False):
    if sit:
        res = moeda(n /2)
        return res
    else:
        res = n /2
        return res


def moeda(n):
    return f'R${n}'


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

