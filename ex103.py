#Minha solução
#def ficha(nome=False, gols=False):
#    if nome:
#        nome = nome
#    else:
#        nome = '<desconhecido>'
#    if gols.isnumeric():
#        gols = int(gols)
#    else:
#        gols = 0
#    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#nome = str(input('Nome do Jogador: '))
#gols = str(input('Números de Gols: '))
#ficha(nome, gols)



#Solução do Professor
def ficha(jog="<desconhecido>", goal=0):
    print(f'O jogador {jog} fez {goal} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Números de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip == '':
    ficha(goal=g)
else:
    ficha(n, g)
