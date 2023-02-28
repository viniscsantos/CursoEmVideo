dados = list()
pessoas = list()
g = list()
maior = menor = 0
while True:
    resp = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while resp not in 'sSnN':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
for c, p in enumerate(pessoas):
    if c == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
