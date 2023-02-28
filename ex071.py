print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
sac = int(input('Que valor você quer sacar? R$ '))
nota = (50, 20, 10, 1)
c = 0
while True:
    if sac // nota[c] > 0:
        nota1 = sac // nota[c]
        sac = sac % nota[c]
        if nota1 > 0:
            print(f'Total de {nota1} cédulas de R$ {nota[c]}')
    c += 1
    nota1 = 0
    if c == 4:
        break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
