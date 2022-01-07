print('-='*20)
times = ('Atlético', 'Palmeiras', 'São Paulo', 'Santos', 'Corinthians',
         'Ceará SC', 'Athético PR', 'Flamengo', 'Chapecoense', 'Bahia',
         'Goiás', 'Botafogo', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Grêmio',
         'Avaí', 'Vasco da Gama', 'CSA', 'Fluminense' )
print('{:=^40}'.format(' CLASSIFICAÇÃO DO BRASILEIRÃO 2019 '))
c = 0
for t in times:
    c += 1
    print(f'{c}º - {t}')
print('-='*20)
print(f'Os 5 primeiros são: {times[0:5]}.')
print('-='*20)
print(f'Os quatros últimos: {times[-4:]}.')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}.')
print('-='*20)
print(f'O Chapecoense está  na {times.index("Chapecoense")+1}ª posição.')
