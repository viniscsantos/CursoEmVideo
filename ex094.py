dados = dict()
pessoas = list()
med = 0
while True:
    resp = ' '
    dados['nome'] = str(input('Nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    med = med + dados['idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {med / len(pessoas):.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p["nome"], end=' ')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] >= (med / len(pessoas)):
        for k, v in p.items():
            print(f'   {k} = {v};', end='')
        print()
print('<< ENCERRADO >>')
