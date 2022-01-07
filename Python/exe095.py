print('='*50)
print(f'{"ANÁLISE FUTEBOLÍSTICA":^50}')
print('='*50)
jogadores = []
analise = {}
gols = []
while True:
    soma = 0
    analise['Jogador'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {analise["Jogador"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'{"=>":>5}Quantos gols na partida {c+1}? ')))
        soma += gols[c]
    analise['Gols'] = gols[:]
    gols.clear()
    analise['Total'] = soma
    jogadores.append(analise.copy())
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    print('-'*50)
    if r in 'Nn':
        break
print('-='*25)
print('cod ', end='')
for k in analise.keys():
    print(f'{k:<15}', end='')
print()
print('='*50)
for i, l in enumerate(jogadores):
    print(f'\n{i+1:<3} ', end='')
    for v in l.values():
        print(f'{str(v):<15}', end='')
print()
print('-='*25)
while True:
    codigo = int(input('Mostrar dados de qual jogador? [999 interrompe] '))-1
    if codigo == 998:
        break
    if codigo >= len(jogadores):
        print('Código inválido! Não existe jogador com esse código.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[codigo]["Jogador"]}:')
        for cod, g in enumerate(jogadores[codigo]['Gols']):
            print(f'{" ":>4}No jogo {cod+1} fez {g} gols.')
    print('=='*25)
print('')
print('<< ATÉ A PRÓXIMA ANÁLISE! >>')







