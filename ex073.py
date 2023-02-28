print('-=' * 20)
lista = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')
print(f'Lista de times do Brasileirão: {lista}')
print('-=' * 20)
print(f'Os 5 primeiros são {lista[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {lista[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-=' * 20)
print(f'O {lista[7]} está na {lista.index("Chapecoense")+1}ª posição')
