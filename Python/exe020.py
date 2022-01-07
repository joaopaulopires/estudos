import random
n1 = input('Participante: ')
n2 = input('Participante: ')
n3 = input('Participante: ')
n4 = input('Participate: ')
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('Atenção alunos: a ordem de apresentação dos trabalhos será: ', alunos)