from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= {"SORTEANDO"} {n} {"JOGOS"} -=-=-=')
for c in range(1, n + 1):
    for cont in range(0, 6):
        num = randint(1, 60)
        while True:
            if num in lista:
                num = randint(1, 60)
            else:
                lista.append(num)
                lista.sort()
                break
    jogos.append(lista[:])
    lista.clear()
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print(f'  -=-=-= < BOA SORTE! > -=-=-=')
