from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sair = False
while not sair:
    print('''    [1] somar 
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    n3 = int(input('>>>>> Qual é a sua opção? '))
    if n3 == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif n3 == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
    elif n3 == 3:
        if n1 < n2:
            print(f'Entre {n1} e {n2} o maior é {n2}')
        elif n1 > n2:
            print(f'Entre {n1} e {n2} o maior {n1}')
        else:
          print('Os dois valores são iguais.')
    elif n3 == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif n3 == 5:
        print('Finalizando...')
        sair = True
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(0.5)
