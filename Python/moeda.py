def aumentar(n, jA=0, sit=False):
    if sit:
        return moeda(n + (n/100) * jA)
    else:
        return n + (n/100) * jA


def diminuir(n, jB=0, sit=False):
    if sit:
        return moeda(n - (n / 100) *jB)
    else:
        return n - (n / 100) *jB


def dobro(n, sit=False):
    if sit:
        return moeda(n * 2)
    else:
        return n * 2


def metade(n, sit=False):
    if sit:
        return moeda(n /2)
    else:
        return n /2


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n}'.replace('.', '.')


def resumo(n, jA, jB):
    print('-'*50)
    print(f'{"RESUMO DO VALOR":^50}')
    print('-'*50)
    print(f'{"Preço analisado:":<40}R${n}')
    print(f'{"Dobro do preço:":<40}{dobro(n, True)}')
    print(f'{"Metade do preço :":<40}{metade(n, True)}')
    print(f'{jA}{"% de aumento:"}{aumentar(n, jA, True):>30}')
    print(f'{jB}{"% de redução:"}{diminuir(n, jB, True):>30}')
    print('-'*50)

