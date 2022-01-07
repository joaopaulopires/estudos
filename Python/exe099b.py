from time import sleep

def maior(*n):
    print('-=' * 25)
    print('Analisando os valores  passados...')
    for c in range(0, len(n)):
        print(n[c], end=' ')
        sleep(0.25)
        if c == 0:
            maior = n[c]
        else:
            if maior < n[c]:
                maior = n[c]
    print(f'Foram informados {maior} valores.' if maior == 0 else f'Foram informados {len(n)} valores.')
    print(end='')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)