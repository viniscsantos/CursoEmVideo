pal = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
       'PYTHON', 'CURSO', 'GRATIS',
       'ESTUDAR', 'PRATICAR', 'TRABALHAR',
       'MERCADO', 'PROGRAMADOR', 'FUTURO')
for cont in pal:
    print(f'\nNa palavra {cont} temos ', end='')
    for letra in cont:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
