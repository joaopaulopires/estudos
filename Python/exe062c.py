print('\33[1;30;41m{}{}{}\33[m'.format('+'*15, ' PROGRESSÃO ARITIMÉTICA ','+'*15))
print(' ')
primeiro = int(input('\33[34;1m Digite o 1º Termo: \33[m '))
razao = int(input('\33[34;1m Digite a Razão: \33[m '))
termo = primeiro
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('\33[1;31m {} \33[1;32m->\33[m'.format(termo), end='')
        termo += razao
        c += 1
    print('\33[1;30mPAUSA\33[m')
    mais = int(input('\n\33[1;34mQuer mostrar mais quantos \33[1;31mTermos? \33[m'))
print('\33[1;34mProgressão finalizada com {} termos mostrados.\33[m'.format(c))
print('\33[1;34mFIM\33[m')
print('\33[30;41;1m+\33[m'*50)