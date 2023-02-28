val = []
for cont in range(0, 5):
    val.append(int(input(f'Digite um valor na Posição {cont}: ')))
print('=-' * 30)
print(f'Você digitou os valores {val}')
print(f'O maior valor digitado foi {max(val)} nas posições', end='')
for c, pos in enumerate(val):
    if pos == max(val):
        print(f' {c}...', end='')
print(f'\nO menor valor digitado foi {min(val)} nas posições', end='')
for c, pos in enumerate(val):
    if pos == min(val):
        print(f' {c}...', end='')
