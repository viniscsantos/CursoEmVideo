sal = float(input('Qual o salário do funcionario? R$'))
print('Um funcionário que ganhava R${:.2f}, com novo aumento, passa a receber R${:.2f}'.format(sal, sal + sal * 15 / 100))