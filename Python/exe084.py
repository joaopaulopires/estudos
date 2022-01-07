print('\33[4;34m{:^40}\33[m'.format(' CADASTRO POSITIVO '))
dados = []
reserva = list()
c = 0
pesada = []
leve = []
while True:
    c += 1
    print('-'*30)
    print(f'{c}º Cadastrado: ')
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(reserva) == 0:
        maior = menor = dados[1]
    else:
        if maior <= dados[1]:
            maior = dados[1]
        if menor >= dados[1]:
            menor = dados[1]
    reserva.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for cad2 in reserva:
    if maior in cad2:
        pesada.append(cad2[0])
    if menor in cad2:
        leve.append(cad2[0])
print(f'Ao todo, você cadastrou {len(reserva)} pessoas.')
print(f'O maior peso foi de {maior}kg.Peso de {pesada}')
print(f'O menor peso foi de {menor}kg. Peso de {leve}')




