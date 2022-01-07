s = 0
s2= 0
for c in range(1,7):
    n = int(input(' Digite um número: '))
    par = n%2
    if par == 0:

        s2 += 1
        s += n
print('A soma dos {} números pares é {}'.format(s2, s))