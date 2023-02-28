from ex108 import moeda

val = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(val)} é {moeda.moeda(moeda.metade(val))}')
print(f'O dobro de {moeda.moeda(val)} é {moeda.moeda(moeda.dobro(val))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(val, 10))}')
