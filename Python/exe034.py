print('{}{:$^50}{}'.format('\33[30;42m',' \33[4;30;42mDISSÍDIO\33[30;42m ','\33[m'))
print('\33[1;31m-\33[m'*50)
sal = float(input('\33[1;32mQual o seu salário atual?\33[m R$ '))
if sal>1250.5:
    reajuste = sal+(sal/100)*10
    print('\33[1;32mPara salários \33[4;31macima de R$1250,00\33[m \33[1;32mo reajuste será de \33[30;41m10%\33[m')
else:
    reajuste = sal+(sal/100)*15
    print('\33[1;32mPara salários \33[4;31migual ou inferior a R$1250,00 \33[1;32mo reajuste será de \33[30;41m15%\33[m')
print('\33[1;32mPortanto, seu salário será reajustado para \33[4;31;40mR${}\33[m'.format(reajuste))
print('\33[1;31m-\33[m'*50)
