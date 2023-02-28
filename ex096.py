def caul(a, b):
    met = a * b
    print(f'A área de um terreno {a}x{b} é de {met}m².')


print('Controle de Terreno')
print('-' * 40)
n1 = float(input('LARGURA (m): '))
n2 = float(input('COMPRIMENTO (m): '))
caul(n1, n2)
