casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
temp = int(input('Quantos anos de financiamento? '))
pres = casa/(temp * 12)
trintsal = sal * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, temp), end='')
print(' a prestação será de R${:.2f}'.format(pres))
if pres <= trintsal:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!')
else:
    print('\033[31mEmpréstimo NEGADO!')

