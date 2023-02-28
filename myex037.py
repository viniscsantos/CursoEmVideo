n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para converção:')
print('[{}] converter para BINÁRIO'.format('1'))
print('[{}] converter para OCTAL'.format('2'))
print('[{}] converter para HEXADECIMAL'.format('3'))
escolha = str(input('Sua opção: '))
#conversão decimal > binário
n2 = 0
n1 = n
n3 = '0'
if n1 >= 1:
   n3 = str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
if n1 >= 1:
   n3 = n3 + str(n1 % 2)
   n1 = n1//2
#conversão decimal > octal
o1 = n
if o1 >= 1:
   o3 = str(o1 % 8)
   o1 = o1//8
if n1 >= 1:
   o3 = o3 + str(o1 % 8)
   o1 = o1//8
if n1 >= 1:
   o3 = o3 + str(o1 % 8)
   o1 = o1//8
if o1 >= 1:
   o3 = o3 + str(o1 % 8)
   o1 = o1//8
if o1 >= 1:
   o3 = o3 + str(o1 % 8)
   o1 = o1//8
if o1 >= 1:
   o3 = o3 + str(o1 % 8)
   o1 = o1//8
if o1 >= 1:
   o3 = o3 + str(o1 % 8)
   o1 = o1//8
#conversão decimal > hexadicimal
h1 = n
if h1 > 1:
   h3 = str(h1 % 16)
   if h3 == '10':
      h3 = 'A'
   elif h3 == '11':
      h3 = 'B'
   elif h3 == '12':
      h3 = 'C'
   elif h3 == '13':
      h3 = 'D'
   elif h3 == '14':
      h3 = 'E'
   elif h3 == '15':
      h3 = 'F'
   h1 = h1 // 16
if h1 > 1:
   h4 = str(h1 % 16)
   if h4 == '10':
      h4 = 'A'
   elif h4 == '11':
      h4 = 'B'
   elif h4 == '12':
      h3 = 'C'
   elif h4 == '13':
      h4 = 'D'
   elif h4 == '14':
      h4 = 'E'
   elif h4 == '15':
      h4 = 'F'
   h1 = h1 // 16
   h3 = h3 + h4
if h1 > 1:
   h4 = str(h1 % 16)
   if h4 == '10':
      h4 = 'A'
   elif h4 == '11':
      h4 = 'B'
   elif h4 == '12':
      h3 = 'C'
   elif h4 == '13':
      h4 = 'D'
   elif h4 == '14':
      h4 = 'E'
   elif h4 == '15':
      h4 = 'F'
   h1 = h1 // 16
   h3 = h3 + h4
if h1 > 1:
   h4 = str(h1 % 16)
   if h4 == '10':
      h4 = 'A'
   elif h4 == '11':
      h4 = 'B'
   elif h4 == '12':
      h3 = 'C'
   elif h4 == '13':
      h4 = 'D'
   elif h4 == '14':
      h4 = 'E'
   elif h4 == '15':
      h4 = 'F'
   h1 = h1 // 16
   h3 = h3 + h4
if escolha == '1':
    print('{} convertido para BINÁRIO é igual a {}'.format(n, n3[::-1]))
elif escolha == '2':
    print('{} convertido para OCTAL é igual a {}'.format(n, o3[::-1]))
elif escolha == '3':
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, h3[::-1]))







