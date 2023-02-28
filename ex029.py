velo = int(input('Qual é a velocidade do carro? '))
if velo > 80:
    multa = (velo - 80) * 7
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de \033[33mR${}!\033[m'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!')
