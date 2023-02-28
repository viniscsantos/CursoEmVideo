mai = men = tot = soma = n = 0
resp = 'S'
while resp in 'sS':
    n = int(input('Digite um número: '))
    if tot == 0:
        mai = men = n
    else:
        if n > mai:
            mai = n
        if n < men:
            men = n
    resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    soma += n
    tot += 1
print(f'Você digitou {tot} números e a média foi {soma/tot:.2f}')
print(f'O maior valor foi {mai} e o menor foi {men}')

