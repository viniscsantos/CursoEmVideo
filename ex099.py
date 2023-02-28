from time import sleep


def maior(*num):
    quant = maior = 0
    print('-=' * 30)
    print('Analizando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.2)
        if quant == 0 or v > maior:
            maior = v
        quant += 1
    print(f'Foram informados {quant} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
