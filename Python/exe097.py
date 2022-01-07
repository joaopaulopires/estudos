def escreva(txt):
    txt.strip()
    b = len(txt)+4
    print('='*b)
    print(f'{txt:^{b}}')
    print('='*b)



while True:
    escreva(str(input('Digite um texto: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Cont?: ')).upper()[0]
    print('-'*50)
    if r in 'N':
        break


