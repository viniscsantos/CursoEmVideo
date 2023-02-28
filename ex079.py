val = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in val:
        print('Valor adicionado com sucesso...')
        val.append(num)
    else:
        print('Valor duplicado! Não vou adicionar.')
    resp = str(input('Quer continuar? '))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(val)}')
