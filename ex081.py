val = []
while True:
    resp = 'd'
    val.append(int(input('Digite um valor: ')))
    while resp not in 'sSnN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'nN':
        break
val.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(val)} elemntos.')
print(f'Os valores em ordem decrecente são {val}')
if 5 in val:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
