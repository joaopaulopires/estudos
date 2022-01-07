from exe107 import moeda

p = float(input('Digite o preço: R$ '))
a = float(input('Aumentar: '))
b = float(input('Baixar: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando {a}%, temos {moeda.aumentar(p, a)}')
print(f'Reduzindo {b}%, temos {moeda.diminuir(p, b)}')
