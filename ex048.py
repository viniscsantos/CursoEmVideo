valor = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        valor += 1
print('\033[33mA soma de todos os {} calores solicitados é {}'.format(valor, soma))


