num = int(input('Digite um número para calcular seu Fatorial:'))
cont = num
result = 1
print((f'Calculando {num}! = '), end='')
while cont > 0:
    print((cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    result *= cont
    cont -= 1
print(result)

