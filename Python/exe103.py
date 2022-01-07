def ficha(n='<desconhecido>', g=0):

    print(f'O jogador {n} fez  {g} gols no campeonato.')


print('-'*40)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input(f'Quantos gols {nome} fez? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)
