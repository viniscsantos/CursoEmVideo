matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somater = maior = 0
for lin in range(0, 3):
    for c in range(0, 3):
        matriz[lin][c] = int(input(f'Digite um valor para [{lin}, {c}]: '))
        if matriz[lin][c] % 2 == 0:
            par += matriz[lin][c]
        if c == 2:
            somater += matriz[lin][c]
        if lin == 1 and c == 0:
            maior = matriz[lin][c]
        elif lin == 1 and matriz[lin][c] > maior:
            maior = matriz[lin][c]
print('-=' * 30)
for lin in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[lin][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {somater}')
print(f'O maior valor da segunda linha é {maior}')
