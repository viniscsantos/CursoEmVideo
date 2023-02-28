#def contador(i, f, p):
#    """
#
#    :param i: início da contagem
#    :param f: fim da contagem
#    :param p: passo da contagem
#    :return: sem retorno
#    """
#    cont = i
#    while cont <= f:
#        print(cont, end=' ')
#        cont += p
#    print('FIM')


#help(contador)


#def somar(a=0, b=0, c=0):
#    """

#    :param a: primeiro valor
#    :param b: segundo valor
#    :param c: terceiro valor
#    :return: sem retorno
#    """
#    s = a + b + c
#    print(f'A soma vale {s}')


#somar()

#def teste(b):
#    global a
#    a = 8
#    b += 4
#    c = 2
#    print(f'A dentro vale {a}')
#    print(f'B dentro vale {b}')
#    print(f'C dentro vale {c}')

#a = 5
#teste(a)
#print(f'A fora vale {a}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


#def par(num=0):
#   if num % 2 == 0:
#      return True
#   else:
#       return False

#n = int(input('Digite um número: '))
#if par(n) == True:
#    print(f'O valor {n} é par!')
#elif par(n) == False:
#    print(f'O valor {n} é ímpar!')






