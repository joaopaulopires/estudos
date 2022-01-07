print('\33[4;35m {}{}{}\33[m'.format('-='*15, ' GÊNERO ', '-='*15))
print(' ')
r = ' '
c = 0
while r != 'N':
    sexo = ' '
    while 'F' != sexo != 'M' :
        sexo = ' '
        sexo = str(input('\33[4;31mInforme o seu sexo: [M/F]\33[m '))
        if 'F' != sexo != 'M':
            c += 1
            print('\33[1;30mOPÇÃO INVÁLIDA {}. \33[m'.format(c), end='')
    print('\33[30mSexo \33[4;31m {} \33[30m registrado com sucesso!\33[m'.format(sexo))
    r = str(input('\33[1;34mQuer continuar? [S/N] \33[m')).upper()
    print(' ')
print('FIM')

print('Versão Guanabara')
sexo = ' '
sexo = str(input('Informe seu sexo: [M/F} ')).strip().upper()[0]
while sexo not in'MmFf':
    sexo = str(input('DADOS INVÀLIDOS. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))