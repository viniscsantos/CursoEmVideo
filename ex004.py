n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um numero? {} '.format(n.isnumeric()))
print('É alfabético? {} '.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiusculas? {}'.format(n.isupper()))
print('Está em minúsculas {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
