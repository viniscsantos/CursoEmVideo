print('---' * 10)
print('      LOJA SUPER BARATÃO')
print('---' * 10)
tot = mai = cont = men = 0
while True:
    pt = str(input('Nome do Produto: '))
    pr = float(input('Preço: R$'))
    tot += pr
    mpt = ''
    if cont == 0 or pr < men:
        men = pr
        mpt = pt
        if pr > 1000:
            mai += 1
    cont += 1
    cnt = ' '
    while cnt not in 'SN':
        cnt = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cnt == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {mai} produtos custando mais de 1000.00')
print(f'O produto mais barato foi {mpt} que custa R${men:.2f}')

