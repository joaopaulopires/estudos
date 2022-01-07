def leiaInt(msg):
    ok = False
    while True:
        try:
            inteiro = str(input(msg))
            inteiro.isnumeric()
            valorInt = int(inteiro)
            if ok:
                break

        except (TypeError, ValueError):
            print('\033[0;31mERRO: Digite um número Inteiro válido.\033[m')
        else:
            return valorInt


def leiaFloat(msg):
    ok = False
    while True:
        try:
            real = str(input(msg)).replace(',', '.')
            if real == '':
                real
            valorReal = float(real)
            if ok:
                break

        except (TypeError, ValueError):
            print('\033[0;31mERRO: Digite um número Real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
        else:

            return valorReal

inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O valor Inteiro digitado foi {inteiro} e o valor Real foi {real}')
