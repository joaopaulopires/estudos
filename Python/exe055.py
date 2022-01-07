print('\33[4;30;41m{}{}{}\33[m'.format('@'*20, ' PESO PESADO ', '@'*20))
maior = 0
menor = 0
for c in range(1, 6):
    n = float(input('\33[4;36mPeso:\33[m '))
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('\33[4;35m{}kg\33[1;35m é o maior peso.\33[m\n\33[4;33m{}kg\33[1;33m é o menor peso.\33[m'.format(maior, menor))
