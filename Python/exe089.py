dado = []
escola = []
c = 0
print('{}{}{}'.format('*'*10, ' ESCOLA PYTHON ', '*'*10))
print('-='*20)
while True:
    dado.append(str(input('NOME: ')))
    escola.append(dado[:])
    dado.clear()
    dado.append(float(input('NOTA 1: ')))
    dado.append(float(input('NOTA 2: ')))
    escola[c].append(dado[:])
    dado.clear()
    c += 1
    r = ' '
    r = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
    print('-'*20)
print('='*30)
print('\33[4;34m  MÉDIA ESCOLAR  \33[m')
print('='*30)
print(f'{"Nº.":<4}{"ALUNOS":<10}{"MÉDIA":>8}')
print('-'*30)
for i, parte in enumerate(escola):
    print(f'{i}- {parte[0]:.<15}{(parte[1][0]+parte[1][1]) / 2: >5}')
print('-='*20)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    for parte in escola:
        if escola.index(parte) == n:
            print(f'ALUNO: {parte[0]} - NOTA 1: {parte[1][0]} e NOTA 2: {parte[1][1]}')
    if n == 999:
        break
    print('<<< VOLTE SEMPRE >>>')
print('')
print('VERSÃO GUANABARA')
ficha = []
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Continuar? [S/N] '))
    if resp in 'Nn':
        break
print('='*30)
print(f'{"Nº.":<4}{"ALUNOS":<10}{"MÉDIA":>8}')
print('-'*30)
for i, f in enumerate(ficha):
    print(f'{i:<4}{f[0]:<10}{f[2]:>8.1f}')
while True:
    opc = int(input('MOstrar qual aluno? (999 para) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<< VOLTE SEMPRE >>>>')