frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
invert = frase[::-1].upper()
print(f'O inverso de {frase} é {invert}')
if frase == invert:
    print('A frase digitada é um palíndormo!')
else:
    print('A frase digitada não é um palíndromo!')





