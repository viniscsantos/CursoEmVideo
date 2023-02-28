import random
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = random.randint(0,2)
import time
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada? '))
if player == 0 or player == 1 or player == 2:
   print('JO')
   time.sleep(0.5)
   print('KEN')
   time.sleep(0.5)
   print('PO')
   print('-=-'*10)
   print('O computador escolheu {}'.format(itens[cpu]))
   print('O jogador escolheu {}'.format(itens[player]))
   if player == 0 and cpu == 1:
      win = 'COMPUTADOR'
   elif player == 1 and cpu == 2:
      win = 'COMPUTADOR'
   elif player == 2 and cpu == 0:
      win = 'COMPUTADOR'
   elif player == 1 and cpu == 0:
      win = 'JOGADOR'
   elif player == 2 and cpu == 1:
      win = 'JOGADOR'
   elif player == 0 and cpu == 2:
      win = 'JOGADOR'
   elif player == cpu:
    win = 'NINGUÉM'
    print('DEU EMPATE. JOGUE NOVAMENTE')
   print('-=-'*10)
   print('{} VENCEU'.format(win))
else:
    print('OPÇÃO INVALIDA. TENTE NOVAMENTE')




