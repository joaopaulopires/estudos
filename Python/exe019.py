from random import choice
print(''
      ''
      '')
n1 = input('Participante 1: ')
n2 = input('Participante 2: ')
n3 = input('Participante 3: ')
n4 = input('Participante 4: ')
escol = (n1, n2, n3, n4)
ven = choice(escol)
print('O escolhido para apagar a lousa foi {}!!!'.format(ven))
