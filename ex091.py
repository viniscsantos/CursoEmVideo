from random import randint
from time import sleep
from operator import itemgetter
print('Valores sorteados: ')
j = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
       'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
for k, v in j.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(j.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.1)