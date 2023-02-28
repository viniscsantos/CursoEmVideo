print('Gerador de PA')
print('-=' * 10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA: '))
cont = 1
termo = n1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += n2
        cont += 1
    print('PAUSA')
    mais = int(input('Qauntos termos você quer mostrar mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
