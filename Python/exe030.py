n = int(input('Digite um número: '))
res = n % 2
if res == 1:
    print('O número {} é IMPAR.'.format(n))
else:
    print('O número {} é PAR.'.format(n))