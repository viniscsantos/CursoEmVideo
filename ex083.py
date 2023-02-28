paren = list()
ap = fp = 0
exp = str(input('Digite a expreção: '))
list(exp)
ap = int(exp.count('('))
fp = int(exp.count(')'))
if ap == fp:
    print('Sua expreção está válida!')
else:
    print('Sua expreção está errada!')
