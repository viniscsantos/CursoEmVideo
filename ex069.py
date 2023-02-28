mai = man = girl = 0
while True:
    print('---' * 10)
    print('     CADASTRE UMA PESSOA')
    print('---' * 10)
    age = int(input('Idade: '))
    sex = ' '
    op = ' '
    while sex not in 'MF':
        sex = str(input('SEXO: [M/F] ')).upper().strip()[0]
    print('---' * 10)
    if age > 18:
        mai += 1
    if sex not in 'F':
        man += 1
    if sex not in 'M' and age < 20:
        girl += 1
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if op not in 'sS':
        break
print(f'Total de pessoas com mais de 18 anos: {mai}')
print(f'Ao todo temos {man} homens cadastrados')
print(f'E temos {girl} mulheres com menos de 20 anos')
