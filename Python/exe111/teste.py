from exe111.utilidadescev import moeda
from exe111.utilidadescev import dado

p = dado.leiaDinheiro('Digite um valor: R$')
a = float(input('Aumentar: '))
b = float(input('Baixar: '))
moeda.resumo(p, a, b)
