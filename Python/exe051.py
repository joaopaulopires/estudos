print('CALCULADORA DE PROGRESSÃO ARITMÉTICA')
primeiro = int(input('Digite o 1º Termo: '))
razao = int(input('Digite a Razão: '))
for primeiro in range(primeiro, primeiro +(11-1)*razao, razao):
    print(primeiro,', ', end='')
