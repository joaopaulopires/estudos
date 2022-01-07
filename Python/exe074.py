from random import randint
lista = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100) )
print(f'Os valores sorteados foram: ', end='')
for n in lista:
    print(n, '', end='')
#Solução CURSO
print(f'\nO maior valor sorteado foi {max(lista)}\nO menor valor sorteado sorteado foi {min(lista)}')
#Solução JP
for c in lista:
    if c == lista[0]:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        elif c < menor:
            menor = c
print(f'\nO maior valor sorteado foi {maior}\nO menor valor sorteado sorteado foi {menor}')
