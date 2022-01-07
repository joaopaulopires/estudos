from datetime import date
print(f'\33[4;34m{"PREVIDÊNCIA":*^20}\33[m')
print()
cad = {}
cad['Nome'] = str(input('Nome/ Sobrenome: '))
ano = int(input('Ano de Nascimento: '))
cad['Idade'] = date.today().year - ano
cad['CTPS'] = int(input('Nº da Carteira de Trabalho (0 não tem): '))
if cad['CTPS'] != 0:
    cad['Contratação'] = int(input('Ano de Contratação: '))
    cad['Salário'] = float(input('Vencimentos: R$ '))
    aposent = (35 - (date.today().year - cad['Contratação']) + cad['Idade'])
    cad['Aposentadoria'] = aposent
else:
    print('Até mais!')
print('-='*25)
for k, v in cad.items():
    if v == cad['Aposentadoria']:
        print(f'\33[4;31m{"=>":>5}Sua {k} será com {v} anos.\33[m')
    else:
        print(f'{"-":>5}{k} igual a {v}')


