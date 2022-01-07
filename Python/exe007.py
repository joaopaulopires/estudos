print('{:=^80}'.format('ESCOLA DE PROGRAMAÇÃO EM PYTHON'))
print('')
nome = input('NOME: ')
nota1 = float(input('Prova 1: '))
nota2 = float(input('Prova 2: '))
m = float(nota1 + nota2)/2
print('O aluno {} na 1ª prova obteve {} e na 2ª prova obteve {}.\nPortanto, a sua média é {:.1f}'.format(nome, nota1, nota2, m))