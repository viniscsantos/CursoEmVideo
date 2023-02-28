import random
print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)
win = 0
while True:
    cpu = random.randint(0, 10)
    player = int(input('Diga um valor: '))
    soma = cpu + player
    pi = str(input('Par ou Ímpar? [P/I] ')).strip()[0].upper()
    print('===' * 10)
    print(f'Você jogou {player} e o computador {cpu}. Total de {soma}', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('===' * 10)
    if pi == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!\nVamos jogar novamente...')
            win += 1
        else:
            print('Você PERDEU!')
            break
    if pi == 'I':
        if soma % 2 == 1:
            print('Você VENCEU')
            win += 1
        else:
            print('Você PERDEU')
            break
    print('=-=' * 10)
print(f'GAME OVER! Você venceu {win} vezes')
