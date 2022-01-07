from datetime import date
print('\33[30;44m{}{}{}\33[m'.format('0'*20,' CONFEDERAÇÃO NACIONAL DE NOTAÇÃO ', '0'*20))
nome = str(input('\33[1;34mAtleta, qual é o seu nome? \33[m'))
ano = int(input('\33[1;34mAno de nascimento: \33[m'))
idade = date.today().year - ano
if idade<=9:
    print('\33[1;30m{}, você tem {} anos e sua categoria será a \33[30;44m MIRIM \33[m'.format(nome, idade))
elif idade<=14:
    print('\33[1;30m{}, você tem {} anos e sua categoria será a \33[30;44m INFANTIL \33[m'.format(nome, idade))
elif idade<=19:
    print('\33[1;30m{}, você tem {} anos e sua categoria será a \33[30;44m JUNIOR \33[m'.format(nome, idade))
elif idade<=25:
    print('\33[1;30m{}, você tem {} anos e sua categoria será a \33[30;44m SÊNIOR \33[m'.format(nome, idade))
elif idade > 25:
    print('\33[1;30m{}, você tem {} anos e sua categoria será a \33[30;44m MASTER \33[m'.format(nome, idade))
print(' ')
print('\33[30;44m{}\33[m'.format('0'*50))