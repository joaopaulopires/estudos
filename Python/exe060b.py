from math import factorial
n = int(input('Digite seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
print(' ')
print('-='*20)



n = int(input('Digite o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))