val = []
par = []
impar = []
while True:
    resp = ' '
    val.append(int(input('Digite um valor: ')))
    while resp not in 'sSnN':
        resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
for n in val:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('-=' * 30)
print(f'A lista completa é {val}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
