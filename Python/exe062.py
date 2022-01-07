print('\33[1;30;41m{}{}{}\33[m'.format('+'*15, ' PROGRESSÃO ARITIMÉTICA ','+'*15))
print(' ')
termo = 0
c = 0
p = 0
v = 0
primeiro = int(input('\33[34;1m Digite o \33[1;31m1º Termo: \33[m '))
razao = int(input('\33[34;1m Digite a \33[1;31mRazão: \33[m '))
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
termo2 = int(input('\n\33[1;34mQuer mostrar mais quantos \33[1;31mTermos? \33[m'))
if termo2 != 0:
    t2 = 0
    p2 = 0
    while t2 != termo2:
        if t2 == 0:
            p2 = p
            p2 = p2 +razao
            t2 +=1
            print('\33[1;31m {} \33[1;32m->\33[m'.format(p2), end='')
        else:
            p2 = p2 + razao
            print(' \33[1;31m {} \33[1;32m->\33[m'.format(p2), end='')
            t2 += 1
    print('\33[1;34mFIM\33[m')
else:
    print('\33[1;34mFIM\33[m')
print('\33[30;41;1m+\33[m'*50)