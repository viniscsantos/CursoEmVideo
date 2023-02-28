sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250.00:
   salfinal = sal + sal * 0.15
else:
   salfinal = sal + sal * 0.10
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, salfinal))
