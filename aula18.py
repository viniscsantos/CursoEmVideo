#teste = list()
#teste.append('Gustavo')
#teste.append(40)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)


#galera = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos')

galera = list()
dados = list()
nome = nome1 = ''
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    if c == 0:
        nome = nome1 = dados[0]
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            nome = dados[0]
            maior = dados[1]
        if dados[1] < menor:
            nome1 = dados[0]
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
print('-' * 30)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos')
print('-' * 30)
print(f'{nome} é o/a mais velho/a com {maior} anos')
print(f'{nome1} é o/a mais novo/a com {menor} anos')
