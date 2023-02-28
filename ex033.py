n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 < n2 and n1 < n2:
    menorn = n1
if n2 < n1 and n2 < n3:
    menorn = n2
if n3 < n1 and n3 < n2:
    menorn = n3
if n1 > n2 and n1 > n3:
    maiorn = n1
if n2 > n1 and n2 > n3:
    maiorn = n2
if n3 > n1 and n3 > n2:
    maiorn = n3
print('O menor numero digitado foi {}'.format(menorn))
print('O maior número digitado foi {}'.format(maiorn))



