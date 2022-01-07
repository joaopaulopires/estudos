from datetime import date
print('{:I^50}'.format(' ANO BISSEXTO '))
print('=-='*25)
ano = int(input('Digite o ano (ou 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('{} É um ano bissexto'.format(ano))
else:
    print('{} NÃO É um ano bissexto.'.format(ano))