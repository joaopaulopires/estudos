print(f'\33[1;31m{" ANÁLISE DE VALORES"}\33[m')
print('\33[1;31m-\33[m'*40)
valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print('-='*40)
print(f'Os valores digitados foram {valores}')
print(f'O valor 9 aparece {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 está na {valores.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados são: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
