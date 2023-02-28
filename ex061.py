print('Gerador de PA')
print('-=-' * 10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão da PA:'))
c = 0
n3 = n1
while c < 10:
    print(f'{n3}', end=' -> ')
    n3 += n2
    c += 1
print('FIM')
