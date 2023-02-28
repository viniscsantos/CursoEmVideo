print('=' * 10)
print('\033[33m10 TERMOS DE UMA PA\033[m')
print('=' * 10)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
n3 = n1 + (10 - 1) * n2
for c in range(n1, n3 + n2, n2):
    print(f'{c}', end=' ->  ')
print('ACABOU')
