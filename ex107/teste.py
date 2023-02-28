from ex107 import moeda

val = float(input('Digite um preço: R$'))
print(f'A metade de R${val} é R${moeda.metade(val)}')
print(f'O dobro de R${val} é R${moeda.dobro(val)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(val, 10)}')
