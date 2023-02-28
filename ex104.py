#print('°' * 30)


#def leiaInt(num):
#    num = input(num)
#    while True:
#        if num.isnumeric():
#            break
#        else:
#            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
#            num = input('Digite um número: ')
#    return num


#n = leiaInt('Digite um número: ')
#print(f'Voçê acabou de digitar o número {n}')


#Solução do Professor:
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print((f'Voçê acabou de digitar o número {n}'))
