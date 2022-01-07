print('\33[1;31;40m{} {} {}\33[m'.format('-='*20, 'ANALISADOR DE PALÍNDROMO ', '-='*20))
frase = input('\33[4;31mEscreva uma frase:\33[m ').strip()
frase1 = frase.upper().split()
real = ''.join(frase1)
inversa = ''
for c in range(len(real)-1, -1, -1):
    inversa += real[c]
print('\33[30mO inverso da frase {} é {}\33[m'.format(real, inversa))
if real == inversa:
    print('\33[1;31m A frase {} é um \33[4;31;40m palíndromo \33[m.'.format(frase))
else:
    print('\33[1;31;m A frase {} \33[4;31m não é um palíndromo \33[m'.format(frase))