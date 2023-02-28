jgd = dict()
tot = list()
jgd['nome'] = str(input('Nome do Jogador: ')).strip()
part = int(input(f'Quantas partidas {jgd["nome"]} jogou? '))
for c in range(1, part+1):
    tot.append(int(input(f'   Quantos gols na partida {c}? ')))
jgd['gols'] = tot
jgd['total'] = sum(tot)
print('-=' * 30)
print(jgd)
print('-=' * 30)
for k, v in jgd.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jgd["nome"]} jogou {part} partidas.')
for c, v in enumerate(tot):
    print(f'    => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jgd["total"]} gols.')
