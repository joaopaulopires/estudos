from random import randint
from time import sleep
#import emoji
print('{:&^50}'.format(' PC X USUÁRIO '))
print('=' * 50)
n = int(input('Vamos jogar? De 0 a 5, em qual número estou pensando? '))
print('E você...')
sleep(2)
aleat = randint(0, 5)
if n == aleat:
    print('GANHOU!!! Parabéns! Eu também pensei no número {}'.format(aleat))
else:
    print('PERDEU... eu pensei no número {}...nada haver com o número {} rs...'.format(aleat, n))
print('Vamos brincar mais uma vez?')

