import random
from time import sleep
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
res = random.randint(0, 5)
n1 = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if n1 == res:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}'.format(res, n1))
