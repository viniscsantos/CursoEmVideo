totage = 0
totwoman = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    totage = totage + idade
    if p == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            man = nome
        if idade < 20 and sexo == 'F':
            totwoman += 1
            menor = idade
print(f'A média de idade do grupo é de {totage/4} anos')
print(f'O homem mais velho tem {maior} anos e se chama {man}.')
print(f'Ao todo são {totwoman} mulheres com menos de 20 anos')














