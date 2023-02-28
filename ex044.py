print('='*10 , 'LOJAS GUANABARA', '='*10)
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))
if op == 1:
    desc = preco - preco * 0.10
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desc))
elif op == 2:
    desc = preco - preco * 0.05
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, desc))
elif op == 3:
     print('Sua compra será parcelada em 2x de R${:.2f} SE JUROS'.format(preco/2))
     print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco))
elif op == 4:
    juros = preco + preco * 0.20
    vezes = int(input('Quantas parcelas? '))
    print('Sua compra parcelada em {}x de R${:.2f} COM JUROS'.format(vezes, juros/vezes))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, juros))
else:
    print('Opção invalida.')