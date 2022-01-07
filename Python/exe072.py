while True:
    extenso = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
    print('-='*20)
    n = int(input('Digite um número de 0 a 20: '))
    while True:
        if n < 0 or n > 20:
            n = int(input('Tente novamente. Digite um número de 0 a 20: '))
        else:
            break
    print(f'\33[4;31m{extenso[n]}\33[m')

    extenso = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente.', end='')
    print(f'\33[4;31m{extenso[n]}\33[m')
    print('='*40)
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('ACABOU!')