n = (int(input('Digite um valor: ')),
     int(input('Digite outro valor:')),
     int(input('Digite mais um valor: ')),
     int(input('Digite o último valor: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1}')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram', end=' ')
for cont in n:
    if cont % 2 == 0:
        print(cont, end=' ')
