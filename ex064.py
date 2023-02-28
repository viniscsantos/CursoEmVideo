n1 = tot = soma = 0
while n1 != 999:
    n1 = int(input('Digite um número[999 oara parar]: '))
    if n1 < 999:
        soma += n1
        tot += 1
print(f'Você digitou {tot} números e a soma entre eles foi {soma}.')
