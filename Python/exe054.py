from datetime import date
me = 0
ma = 0
s = 1
for c in range(1,8):
    ano = int(input('{} - Ano de nascimento: '.format(s)))
    s +=1
    #print(date.today().year)
    idade = date.today().year - ano
    if idade < 18:
        me +=1
    elif idade >= 18:
        ma +=1
print('{} cadastrados ainda não atingiram a maioridade. \nE {} cadastrados já são maiores de idade.'.format(me, ma))