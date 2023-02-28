num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')
while True:
    op = False
    resp = ''
    n = int(input('Digite um número: '))
    if n in range(0, 21):
        print(f'Você digitou o número {num[n]}')
    else:
        print('Tente novamente.', end='')
        op = True
    while op is False:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            op = True
        else:
            op = False
    if resp == 'N':
        break
