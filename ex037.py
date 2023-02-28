num = int(input('Digite um número inteiro: '))
print('''Escolha uma da bases para converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua opçaõ: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')
