aluno = []
dados = []
while True:
    resp = ' '
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    aluno.append(dados[:])
    dados.clear()
    while resp not in 'sSnN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No."} {"NOME"} {"MÉDIA":>12}')
print('-' * 30)
for i, l in enumerate(aluno):
    print(f'{i}   {l[0]:<12}', end='')
    print(f'{(l[1] + l[2]) / 2:>5}')
print('-' * 30)
while resp != 999:
    resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp == 999:
        break
    elif resp <= len(aluno):
        print(f'Notas de {aluno[resp][0]} são {aluno[resp][1:]}')
        print('-' * 30)
    else:
        print('Opção invalida. Tente novamente!')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
