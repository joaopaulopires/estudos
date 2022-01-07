print('\33[1;36m-\33[m'*50)
print('\33[1;36m{}{}{}\33[m'.format('='*20, ' TABUADA GERAL ', '='*20))
print('\33[1;36m-\33[m'*50)
while True:
    n = int(input('\33[1;34mQuer ver a tabuada de qual valor?\33[m'))
    print('\33[1;36m-\33[m'*50)
    if n < 0:
        break
    for c in range(0, 11):
        print(f'\33[1;31m{n} X {c:>3} = {n*c:>3}\33[m')
    print('\33[1;36m=\33[m' * 50)
print('\33[7;30mPROGRAMA TABUADA GERAL ENCERRADO Volte sempre!\33[m')