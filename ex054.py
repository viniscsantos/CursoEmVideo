from datetime import date
maior = 0
menor = 0
for cont in range(1, 8):
    data = int(input(f'Em que ano a {cont}° pessoa nasceu? '))
    if date.today().year - data >= 18:
        maior += 1
    else:
        menor += 1
print('')
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também {menor} pessoas menores de idade')

