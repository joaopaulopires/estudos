def helpython():
    n = 'SISTEMA DE AJUDA PyHELP'
    b = len(n)+4
    print('\33[1;30;42m^' * b)
    print(f'\33[1;30;42m{n:^{b}}')
    print('\33[1;30;42m^' * b)

def acesso(resp):
    from time import sleep
    n = f'Acessando o manual do comando {resp}'
    b = len(n)+4
    print('\33[1;30;44m^' * b)
    print(f'\33[1;30;44m{n:^{b}}')
    print('\33[1;30;44m^' * b)
    sleep(1)
    print('\33[7;30m')
    help(resp)

while True:
    helpython()
    ajuda = str(input('\33[mFunção ou Biblioteca: '))
    if ajuda in 'fim':
        b = len('ATÉ LOGO!') + 4
        print('\33[1;30;41m^' * b)
        print(f'\33[1;30;41m{"ATÉ LOGO!":^{b}}')
        print('\33[1;30;41m^' * b)
        break
    acesso(ajuda)

