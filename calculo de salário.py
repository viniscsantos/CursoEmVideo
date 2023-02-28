print(f"\033[34m{'CALCULO DE SALÁRIO':=^60}\033[m")
pont = float(input('\033[1;29mDigite sua pontuação: \033[m'))
com = pont * 0.135804
base = 0
cat = str(input('\033[1;29mDigite sua categoria: \033[m'))
if cat == 'a':
    base = 1650
if cat == 'b':
    base = 1060
if cat == 'c':
    base = 749
if cat == 'borracheiro':
    base = 749
print('\033[7mSeu salário bruto será {:.2f}\033[m'.format(com + base))
