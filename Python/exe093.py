print('='*50)
print(f'{"ANÁLISE FUTEBOLÍSTICA":^50}')
print('='*50)
analise = {}
gols = []
soma = 0
analise['Jogador'] = str(input('Nome do Jogador: '))
analise['Partidas'] = int(input(f'Quantas partidas {analise["Jogador"]} jogou? '))
print('-'*50)
for c in range(0, analise['Partidas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    soma += gols[c]
analise['Gols'] = gols[:]
analise['Total'] = soma
print('-'*50)
print(analise)
print('-='*25)
for k, v in analise.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)
print(f'O jogador {analise["Jogador"]} jogou {analise["Partidas"]} partidas.')
for i, c in enumerate(analise['Gols']):
    print(f'{"=>":>4} Na partida {i+1}, fez {c}')
print(f'Foi um total de {analise["Total"]} gols.')




