n1 = int(input('Digite um número: '))
soma = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end=(' '))
        soma = soma + 1
    else:
        print('\033[31m', end=(' '))
    print((c), end=(' '))
print(f'\n\033[mO número {n1} foi divisível {soma} vezes')
if soma == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')



