from datetime import date
sexo = int(input('''Qual é o seu sexo?
[ 1 ] Masculino
[ 2 ] Feminino '''))
if sexo == 1:
     ano = int(input('Ano de nacimento: '))
     date = date.today().year
     idade = date - ano
     print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, date))
     if idade < 18:
         rest = 18 - idade
         print('Ainda faltam {} anos para o alistamento.'.format(rest))
         print('Seu alistamento será em {}'.format(date + rest))
     elif idade > 18:
         rest = idade - 18
         print('Você já deveria ter se alistado há {} anos.'.format(rest))
         print('Seu alistamento foi em {}'.format(date - rest))
     else:
         print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo == 2:
    print('Você não precisa fazer alistamento obrigatório.')
else:
    print('Opção errada. Escolha novamente!')






