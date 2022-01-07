def notas(n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    s = 0
    aluno = dict()
    aluno['Total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    aluno['Média'] = sum(n) / len(n)
    if sit:
        if aluno['Média'] > 7:
            aluno['Situação'] = 'BOA'
        elif aluno['Média'] >= 5:
            aluno['Situação'] = 'REGULAR'
        else:
            aluno['Situação'] = 'RUIM'
    return aluno

l = []
c = n = 0
while True:
    c +=1
    n = float(input(f'Digite a nota {c} [999 interrompe]'))
    if n == 999:
        break
    l.append(n)

print(notas(l, sit=True))
help(notas)
