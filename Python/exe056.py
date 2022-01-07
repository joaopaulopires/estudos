print('\33[4;30;43m-=\33[m'*20)
print('\33[31m {:^40} \33[m'.format('ANALISADOR'))
print('\33[4;30m-=\33[m'*20)
s = 0
maior = 0
cont = 0
velho = ''
for c in range(1,5):
    print('\33[1;31m{} {}{} {}\33[m'.format('-'*10, c,'ª PESSOA', '-'*10))
    nome = str(input('\33[30;4mNOME:\33[m ')).strip()
    idade = int(input('\33[30;4mIDADE:\33[m '))
    sexo = str(input('\33[30;4mSEXO:[M/F]\33[m ')).strip().upper()
    print(' ')
    s += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            velho = nome
    if sexo == 'F':
        if idade < 20:
            cont += 1
print('\33[1;34mA média de idade do grupo é \33[4;34m{} anos.\33[m\n\33[4;32m{}\33[1;32m é o homem mais velho do grupo. Ele tem \33[4;32m{} anos.\33[m'.format((s/4)//1, velho, maior))
if cont > 1:
    print('\33[1;36mE o grupo tem \33[4;36m{} mulheres\33[1;36m com menos de 20 anos.\33[m'.format(cont))
else:
    print('\33[1;36mE o grupo tem \33[4;36m{} mulher\33[1;36m com menos de 20 anos.\33[m'.format(cont))
print(' ')
print('\33[4;30;43m-=\33[m'*20)