val = list()
for cont in range(0, 5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > val[-1]:
        val.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(val):
            if num <= val[pos]:
                val.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {val}')
