
def voto(id):
    from datetime import date
    idade = date.today().year - id
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('VOTO NEGADO.')
    elif 16 <= idade < 18 or idade > 65:
        print(' VOTO OPCIONAL.')
    elif 65 > idade >= 18:
        print('VOTO OBRIGATÓRIO!')


print('-'*40)
ano = int(input('Em que ano você nasceu? '))
voto(ano)
