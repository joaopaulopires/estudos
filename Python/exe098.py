from time import sleep


def contador(a, b, c):
    if c <= 0:
        c *= -1
    if c == 0:
        c = 1
    print('-='*25)
    print(f'Contagem de {a} até {b} de {c} em {c} ')
    sleep(2.5)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= c
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*25)
print('Agora é a sua vez de personalizar a contagem: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)



