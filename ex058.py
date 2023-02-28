import random
cpu = random.randint(0, 10)
print('''Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
tent = 0
while not acertou:
    player = int(input('Qual é o seu palpite? '))
    tent += 1
    if player == cpu:
        acertou = True
    else:
         if player < cpu:
             print('Mais... Tente mais uma vez.')
         elif player > cpu:
             print('Menos... Tente mais uma vez.')
print(f'Acertou com {tent} tentativas. Parabéns!')




