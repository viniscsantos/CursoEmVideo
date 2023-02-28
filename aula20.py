# def mensagem(msg):
#    print('-' * 30)
#    print(msg)
#    print('-' * 30)


# mensagem(f'{"Sitema de Alunos":^30}')


#def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma de {a} e {b} é {s}')


#soma(a=2, b=3)
#soma(b=4, a=2)

#def cont(* núm):
#    for v in núm:
#        print(f'{v} ', end='')
#    print('FIM')

#cont(7, 1, 3)


#def cont(* num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} números.')

#cont(7, 8)
#cont(8, 6)


#def dobra(lst):
#   pos = 0
#   while pos < len(lst):
#       lst[pos] *= 2
#       pos += 1


#valores = [6, 3, 9, 1, 0, 2]
#dobra(valores)
#print(valores)


def soma(* v):
    s = 0
    for c in v:
        s += c
    print(f'Somando os valores {v} temos {s}')


soma(2, 3)
soma(9, 7, 4)



































