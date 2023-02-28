nome = input('Digite seu nome: ').strip()
recort = nome.split()
print('Seu primeiro nome é {}'.format(recort[0]))
#n1 = len(nome)
#n2 = nome.rfind(' ')
#print('Seu último nome é{}'.format(nome[n2:n1]))
print('Seu último nome é {}'.format(recort[len(recort)-1]))

