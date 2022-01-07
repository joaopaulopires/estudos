print('\33[1;30;41m{}{}{}\33[m'.format('+'*15, ' PROGRESSÃO ARITIMÉTICA ','+'*15))
print(' ')
termo = 0
primeiro = int(input('\33[34;1m Digite o 1º Termo: \33[m '))
razao = int(input('\33[34;1m Digite a Razão: \33[m '))
while termo != 10:
    if termo == 0:
        p = primeiro
        p = p + razao
        termo += 1
        print('\33[1;31m {} \33[1;32m->\33[m'.format(p), end='')
    else:
        p = p + razao
        print('\33[1;31m {} \33[1;32m->\33[m'.format(p), end='')
        termo += 1
print('\33[1;34mFIM\33[m')
print('\33[30;41;1m+\33[m'*50)