print('\33[30;46m^\33[m'*50)
print('\33[7;33;44m{:^^50}\33[m'.format(' CONDIÇÃO TRIANGULAR '))
print('\33[30;46m^\33[m'*50)
r1 = float(input('\33[4;30mReta 1:\33[m '))
r2 = float(input('\33[4;30mReta 2:\33[m '))
r3 = float(input('\33[4;30mReta 3:\33[m '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('\33[30;42mÉ possível formar um triângulo com as 3 retas.\33[m')
    if r1==r2 and r1==r3:
        print('\33[30mE como todos os seus lados são iguais, ele é um \33[30;43mTriângulo Equilátero\33[m')
    elif r1==r2 and r1!=r3 or r2==r3 and r2!=r1 or r3==r1 and r3!=r2:
        print('\33[30mE como apenas dois lados são iguais, ele é um \33[30;45mTriângulo Isósceles\33[m')
    elif r1!=r2 and r1!=r3 and r2!=r3:
        print("\33[30mE como todos os seus lados são diferentes, ele é um \33[30;46mTriângulo Escaleno\33[m")
else:
    print('\33[30;41mNão é possível formar um triângulo com essas 3 retas.\33[m')