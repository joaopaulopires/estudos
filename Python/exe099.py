def maior(l):
    print('-='*25)
    print('Analisando os valores  passados...')
    for c in range(0, len(l)):
        print(l[c], end=' ')
        if c == 0:
            maior = l[c]
        else:
            if maior < l[c]:
                maior = l[c]
    print(f'Foram informados {len(l)} valores.')
    print(end='')
    print(f'O maior valor informado foi {maior}')




lista = []
while True:
    print('-'*50)
    resp = str(input('Montar parâmetros? [S/N] ')).upper()[0]
    if resp in 'N':
        break
    while True:
        temp = int(input('Digite um valor: (999 interrompe)'))
        if temp == 999:
            break
        else:
            lista.append(temp)
    print(lista)
    maior(lista)
    lista.clear()
print('<<< OBRIGADO POR SUA PARTICIPAÇÃO! >>>')

