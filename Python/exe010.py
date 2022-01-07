print('{:=^60}'.format(' CONVERSOR DE MOEDAS '))
n = float(input('Quantos reais você quer converter ? R$ '))
d = float(input('Cotação do dólar: US$ '))
r = n/d
print('Conversão:')
print('Com a cotação do dólar a R$ {:.2f}, você terá US$ {:.2f}.'.format(d, r))