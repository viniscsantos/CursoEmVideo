from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
if idade < 0:
    print('Esse atleta veio do futuro!')
else:
    print('O atleta tem {} anos.'.format(idade))
    if idade <= 9:
       cls = 'MIRIM'
    elif idade <= 14:
       cls = 'INFANTIL'
    elif idade <= 19:
       cls = 'JÚNIOR'
    elif idade <= 25:
       cls = 'SÊNIOR'
    elif idade > 25:
       cls = 'MASTER'
    print('Classificação: {}'.format(cls))



