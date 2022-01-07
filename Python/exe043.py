print('\33[4;31;40m{}{}{}\33[m'.format('=-'*10, ' CÁLCULO DE IMC ', '=-'*10))
nome = str(input('\33[1;34mQual é o seu nome?\33[m '))
peso = float(input('\33[1;34mQuanto você pesa?\33[m '))
altura = float(input('\33[1;34mQual é a sua altura?\33[m '))
imc = peso/(altura**2)
if imc<18.5:
    print('\33[30m{}, o seu IMC está em {:.2f}, portanto você está \33[4;30mAbaixo do Peso.\33[m'.format(nome, imc))
elif imc>=18.5 and imc<25:
    print('\33[30m{}, o seu IMC está em {:.2f}, portanto você está com o \33[4;30mPeso Ideal!\33[m'.format(nome, imc))
elif imc>=25 and imc<30:
    print('\33[30m{}, o seu IMC está em {:.2f}, portanto você está com \33[4;30mSobrepeso.\33[m'.format(nome, imc))
elif imc>=30 and imc<40:
    print('\33[30m{}, o seu IMC está em {:.2f}, portanto você está com \33[4;30mObesidade.\33[m'.format(nome, imc))
else:
    print('\33[30m{}, o seu IMC está em {:.2f}, portanto você está com \33[4;31mObesidade Mórbida.\33[30mProcure um médico.\33[m'.format(nome, imc))
print('\33[4;31;40m{}\33[m'.format('=-'*50))