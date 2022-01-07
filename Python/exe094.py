print(f'\33[4;30m {" ANÁLISE DE CADASTRO ":^50}\33[m')
print('='*50)
cad = dict()
lista = list()
mulher = []
idade = 0
idademedia = []
while True:
    cad['Nome'] = str(input('\33[1;34mNome/ Sobrenome: \33[m')).strip()
    while True:
        cad['Sexo'] = str(input('\33[1;34mSexo: [M/F] \33[m')).strip().upper()[0]
        if cad['Sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F')
    cad['Idade'] = int(input('\33[1;34mIdade: \33[m'))
    idade += cad['Idade']
    lista.append(cad.copy())
    while True:
        r = str(input('\33[1;34mContinuar? [S/N] \33[m')).upper()[0]
        if r in 'SN':
            break
    if r in 'N':
        break
    print('\33[1;34m-\33[m' * 50)
print('\33[1;34m-=\33[m'*25)
print(f'\33[1;31m{"=>":^5} O grupo tem {len(lista)} pessoas cadastradas.\33[m')
print(f'\33[1;31m{"=>":^5} A média de idade é de {idade/len(lista):5.2f} anos.\33[m')
print(f'\33[1;31m{"=>":^5} As mulheres cadastradas foram: \33[m', end='')
for l in lista:
    if l['Sexo'] in 'F':
        mulher.append(l['Nome'][:])
        print(f'{l["Nome"]}', end='')
print()
print(f'\33[1;31m{"=>":^5} Lista de pessoas que estão acima da média: \33[m')
for l in lista:
    if l['Idade'] >= idade/len(lista):
        print(f'{" ":>10}', end='')
        idademedia.append(l.copy())
        for k, v in l.items():
            print(f'\33[1;31m{k} = {v}; \33[m', end='')
        print('')
print('')
print(lista)
print(mulher)
print(idademedia)




