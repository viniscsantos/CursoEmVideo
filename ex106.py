from time import sleep

c = ('\033[m',  # 0 - sem cor
     '\033[29;41m',  # 1 - vermelho
     '\033[29;42m',  # 2 - verde
     '\033[29;44m',  # 3 - azul
     '\033[7;40m',  # 4 - branco
     )


def ajuda(op):
    titulo(f"Acessando o manual do comando '{op}'", 3)
    print(c[4], end='')
    help(op)
    print(c[0], end='')
    sleep(0.5)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    resp = str(input('Função ou Biblioteca > '))
    if resp.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    ajuda(resp)
