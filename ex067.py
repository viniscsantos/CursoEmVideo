while True:
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n1 < 0:
        break
    c = 1
    while c <= 10:
       print(f'{n1} x {c} = {n1 * c}')
       c += 1
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
