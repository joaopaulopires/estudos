print('\33[1;30;41m{:=^50}\33[m'.format(' BOLETIM '))
nome = str(input('\33[4;32mNome do aluno:\33[m ')).upper()
n1 = float(input('\33[32mDigite a \33[4;32mnota 1:\33[m '))
n2 = float(input('\33[32mDigite a \33[4;32mnota 2:\33[m '))
n3 = float(input('\33[32mDigite a \33[4;32mnota 3:\33[m '))
media = (n1 + n2 + n3) / 3
if media >= 7 :
    print('\33[1;30;46mParabéns {}! Sua média foi {:.2f} e você foi \33[4;30;46mAPROVADO(a) com louvor!!!\33[m'.format(nome, media))
elif 7> media >= 5:
    print('\33[30;1m{} sua média foi {:.2f} e você está de \33[4;30m RECUPERAÇÃO \33[30;1m, precisa se dedicar mais.\33[m'.format(nome, media))
else:
    print('\33[31;1mSua média foi {:.2f}, portanto abaixo da nota de corte...{} você foi \33[4;31mREPROVADO(a)\33[m.'.format(media, nome))