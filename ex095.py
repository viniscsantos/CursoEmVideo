jgd = dict()
gols = list()
time = list()
while True:
    gols.clear()
    jgd['jogador'] = str(input('Nome do Jogador: ')).strip()
    part = int(input(f'Quantas partidas {jgd["jogador"]} jogou? '))
    for c in range(1, part + 1):
        gols.append(int(input(f'   Quantos gols na partida {c}? ')))
        jgd['gols'] = gols.copy()
    jgd['total'] = sum(jgd['gols'])
    time.append(jgd.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"cod":>4} ', end='')
for i in jgd.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for c, j in enumerate(time):
    print(f'{c:>4} ', end='')
    for d in j.values():
       print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    op = int(input('Mostrar os dados de qual jogador? (999) para parar) '))
    if op == 999:
        break
    elif op >= len(time):
        print(f'ERRO! Não existe jogador com o código {op}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[op]["jogador"]}:')
        for c, v in enumerate(time[op]['gols']):
           print(f'No jogo {c + 1} fez {v} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')









