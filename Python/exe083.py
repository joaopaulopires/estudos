'''print('\33[4;35m{:^40}\33[m'.format(' EXPRESSÕES ERRADAS '))
frase = []
r = str(input('\33[7;30m Digite a expressão: \33[m'))
for c in range(0, len(r)):
    frase.append(r[c])
if frase.count('(') == frase.count(')'):
    print('\33[1;34mExpressão correta!\33[m')
else:
    print('\33[1;31mSua expressão está errada!\33[m')'''
print(' ')
expr = str(input('\33[7;30m Digite a expressão: \33[m'))
pilha =[]
for simb in expr:
    if simb == '(':
        pilha.append('(')

    elif simb ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\33[1;34mExpressão correta!\33[m')
else:
    print('\33[1;31mSua expressão está errada!\33[m')



