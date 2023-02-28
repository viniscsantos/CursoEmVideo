ficha = list()
while True:
    resp = ' '
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    ficha.append([nome, [n1, n2], media])
    while resp not in 'sSnN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"N°":<5}{"NOME":<5}{"MÉDIA":>10}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<10}{a[2]:>5.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostra notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    elif opc < len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        print('Opção invalida. Tente novamente!')
print('<<< VOLTE SEMPRE >>>')
