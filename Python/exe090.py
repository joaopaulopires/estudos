boletim = {}
boletim['Nome'] = str(input('Nome do aluno: '))
boletim['Media'] = float(input(f'Média de {boletim["Nome"]}: '))
print('-='*25)
if boletim['Media'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Media'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
for k, v in boletim.items():
    print(f'{"-":>5}{k:<10} é igual a {v:<10}.')


print(boletim)
