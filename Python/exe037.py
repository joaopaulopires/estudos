
print('\33[7;30m{:=^40}\33[m'.format(' CONVERSOR DE BASES NUMÉRICAS '))
n = int(input('\33[1;31mDigite um número inteiro para conversão:\33[m '))
print('\33[1;30;46mConverter par BINÁRIO  {:>7}\33[m\n\33[1;30;45mConverter para OCTAL {:>9}\33[m\n\33[1;30;42mConverter para HEXADECIMAL {:>3}\33[m'.format('(1)','(2)','(3)'))
base = int(input('\33[1;30mEscolha a Base de Conversão:\33[m '))

if base == 1:
    print('\33[1;30m{} \33[30mconvertido para Base Binária: \33[1;30;46m{}\33[m'.format(n, bin(n)[2:]))
elif base == 2:
    print('\33[1;30m{} \33[30mconvertido para Base Octal: \33[1;30;45m{}\33[m'.format(n, oct(n)[2:]))
elif base == 3:
    print('\33[1;30m{} \33[30mconvertido para Base Hexadecimal: \33[1;30;42m{}\33[m'.format(n, hex(n)[2:]))
else:
    print('\33[7;30m   OPÇÃO INVÁLIDA!   \33[m')
