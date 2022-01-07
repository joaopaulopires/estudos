from time import sleep
c = ('\33[m',                # 0 - sem cores
     '\33[0;30;41m',         # 1 - vermelho
     '\33[0;30;42m',         # 2 - verde
     '\33[0;30;43m',         # 3 - amarelo
     '\33[0;30;44m',         # 4 - azul
     '\33[0;30;45m',         # 5 - roxo
     '\33[7;30m',            # 6 - branco
     '\33[0;30;46m'          # 7 - lilás
     )


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
