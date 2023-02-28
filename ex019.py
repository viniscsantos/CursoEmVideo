import random
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
list = [a, b, c, d]
res = random.choice(list)
print('O aluno escolhido foi {}! '.format(res))
