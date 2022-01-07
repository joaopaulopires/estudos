from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = []
print('-='*15)
print('\33[4;30m Valores Sorteados: \33[m')
for c in range(1, 5):
    jogo[f'Jogador {c}'] = randint(1, 6)
for k, v in jogo.items():
    sleep(0.5)
    print(f'O {k} tirou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*15)
print(ranking, ' <= gera uma Lista com várias Tuplas')
print(f'{" RANKING DOS JOGADORES ":=^30}')
for i, n in enumerate(ranking):
    sleep(0.5)
    print(f'{"*":>4}{i+1}º lugar: {n[0]} com {n[1]}')


print(jogo)
