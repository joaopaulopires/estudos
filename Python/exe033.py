print('{:#^50}'.format(' MAIOR E MENOR '))
print('-'*50)
n1 = float(input('1º Número: '))
n2 = float(input('2º Número: '))
n3 = float(input('3º Número: '))
if n1>n2 and n1>n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
else:
    #n3>n1 and n3>n2:
    maior = n3
if n1<n2 and n1<n3:
    menor = n1
elif n2<n1 and n2<n3:
    menor = n2
else:
    menor = n3
print('{} é o número maior'.format(maior))
print('E {} é o número menor'.format(menor))