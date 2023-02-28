from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')


cont(1, 10, 1)
cont(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
cont(ini, fim, pas)

