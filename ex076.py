print('-' * 30)
print(f'{"LISTAGEM DE PREÇO":^30}')
print('-' * 30)
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
for cont in range(0, len(lista)):
    if cont % 2 == 0:
        print(f'{lista[cont]:.<30}R$', end='')
    else:
        print(f'{lista[cont]:>7.2f}')
